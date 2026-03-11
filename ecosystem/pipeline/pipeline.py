"""
Legal Case Pipeline Orchestrator
LexRexHGNN - Legal Hypergraph Neural Network

Orchestrates the full analysis pipeline across all repositories:
revstream1, ad-res-j7, chainlex, fincosys, and LexRexHGNN.
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path


class LegalCasePipeline:
    """
    Orchestrates the full legal case analysis pipeline.

    Stages:
    1. Validate data contracts (revstream1)
    2. Load ChainLex legal knowledge
    3. Load financial evidence (fincosys)
    4. Construct multi-repository hypergraph
    5. Run neuro-symbolic analysis (LexiCog)
    """

    def __init__(self, workspace: str = "/home/user", config_path: Optional[str] = None):
        self.workspace = workspace
        self.config = {}
        self.results = {}
        self.stage_status = {}

        # Load ecosystem config if provided
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                self.config = json.load(f)
        else:
            # Try default location
            default_config = os.path.join(
                workspace, "LexRexHGNN", "config", "ecosystem.json"
            )
            if os.path.exists(default_config):
                with open(default_config, 'r') as f:
                    self.config = json.load(f)

        # Set up repo paths from workspace
        self.repo_paths = {
            "revstream1": os.path.join(workspace, "revstream1"),
            "ad-res-j7": os.path.join(workspace, "ad-res-j7"),
            "chainlex": os.path.join(workspace, "chainlex"),
            "fincosys": os.path.join(workspace, "fincosys"),
            "LexRexHGNN": os.path.join(workspace, "LexRexHGNN"),
        }

        # Override with config paths if available
        if "repositories" in self.config:
            for name, info in self.config["repositories"].items():
                resolved = os.path.normpath(
                    os.path.join(self.repo_paths["LexRexHGNN"], info["path"])
                )
                self.repo_paths[name] = resolved

    def _log(self, stage: str, message: str):
        """Log a pipeline message."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] [{stage}] {message}")

    def validate_data_contracts(self) -> bool:
        """
        Run revstream1/contracts/validate_contracts.py.

        Returns:
            True if all contracts pass validation.
        """
        self._log("CONTRACTS", "Validating data contracts...")
        self.stage_status["validate_data_contracts"] = "running"

        validate_script = os.path.join(
            self.repo_paths["revstream1"], "contracts", "validate_contracts.py"
        )

        if not os.path.exists(validate_script):
            self._log("CONTRACTS", f"Validation script not found: {validate_script}")
            self.stage_status["validate_data_contracts"] = "skipped"
            return True  # Skip if not found, don't block pipeline

        try:
            result = subprocess.run(
                [sys.executable, validate_script],
                capture_output=True,
                text=True,
                cwd=self.repo_paths["revstream1"],
                timeout=120
            )

            if result.returncode == 0:
                self._log("CONTRACTS", "All data contracts validated successfully")
                self.stage_status["validate_data_contracts"] = "passed"
                self.results["contracts"] = {
                    "status": "passed",
                    "output": result.stdout.strip()
                }
                return True
            else:
                self._log("CONTRACTS", f"Validation failed:\n{result.stderr}")
                self.stage_status["validate_data_contracts"] = "failed"
                self.results["contracts"] = {
                    "status": "failed",
                    "output": result.stdout.strip(),
                    "errors": result.stderr.strip()
                }
                return False

        except subprocess.TimeoutExpired:
            self._log("CONTRACTS", "Validation timed out after 120s")
            self.stage_status["validate_data_contracts"] = "timeout"
            return False
        except Exception as e:
            self._log("CONTRACTS", f"Validation error: {e}")
            self.stage_status["validate_data_contracts"] = "error"
            return False

    def load_chainlex_knowledge(self) -> Dict[str, Any]:
        """
        Load ChainLex legal knowledge base.

        Runs chainlex/exports/export_for_integration.py if exports don't exist.

        Returns:
            Dict with counts of principles/rules loaded.
        """
        self._log("CHAINLEX", "Loading ChainLex legal knowledge...")
        self.stage_status["load_chainlex_knowledge"] = "running"

        chainlex_path = self.repo_paths.get("chainlex", "")
        exports_dir = os.path.join(chainlex_path, "exports")
        result_counts = {"principles": 0, "rules": 0, "frameworks": 0}

        # Run export script if exports don't exist
        if not os.path.exists(exports_dir) or not os.listdir(exports_dir):
            export_script = os.path.join(exports_dir, "export_for_integration.py")
            if os.path.exists(export_script):
                self._log("CHAINLEX", "Running export script...")
                try:
                    subprocess.run(
                        [sys.executable, export_script],
                        capture_output=True,
                        text=True,
                        cwd=chainlex_path,
                        timeout=120
                    )
                except Exception as e:
                    self._log("CHAINLEX", f"Export script error: {e}")

        # Load exported files
        if os.path.exists(exports_dir):
            for filename in os.listdir(exports_dir):
                if not filename.endswith(".json"):
                    continue
                filepath = os.path.join(exports_dir, filename)
                try:
                    with open(filepath, 'r') as f:
                        data = json.load(f)

                    if "principles" in data or "principle" in filename.lower():
                        count = len(data) if isinstance(data, list) else len(data.get("principles", []))
                        result_counts["principles"] += count
                    elif "rules" in data or "rule" in filename.lower():
                        count = len(data) if isinstance(data, list) else len(data.get("rules", []))
                        result_counts["rules"] += count
                    elif "framework" in filename.lower():
                        result_counts["frameworks"] += 1

                    self._log("CHAINLEX", f"Loaded: {filename}")
                except Exception as e:
                    self._log("CHAINLEX", f"Error loading {filename}: {e}")
        else:
            self._log("CHAINLEX", "ChainLex exports directory not found")

        self.stage_status["load_chainlex_knowledge"] = "completed"
        self.results["chainlex"] = result_counts
        self._log("CHAINLEX", f"Loaded {result_counts['principles']} principles, "
                  f"{result_counts['rules']} rules, {result_counts['frameworks']} frameworks")
        return result_counts

    def load_financial_evidence(self) -> Dict[str, Any]:
        """
        Load financial evidence from fincosys exports.

        Returns:
            Dict with counts of loaded financial data.
        """
        self._log("FINCOSYS", "Loading financial evidence...")
        self.stage_status["load_financial_evidence"] = "running"

        fincosys_path = self.repo_paths.get("fincosys", "")
        exports_dir = os.path.join(fincosys_path, "exports")
        result_counts = {
            "reconciliations": 0,
            "transactions": 0,
            "analyses": 0,
            "files_loaded": 0
        }

        if os.path.exists(exports_dir):
            for filename in os.listdir(exports_dir):
                if not filename.endswith(".json"):
                    continue
                filepath = os.path.join(exports_dir, filename)
                try:
                    with open(filepath, 'r') as f:
                        data = json.load(f)

                    result_counts["files_loaded"] += 1

                    if "reconciliation" in filename.lower():
                        count = len(data) if isinstance(data, list) else 1
                        result_counts["reconciliations"] += count
                    elif "transaction" in filename.lower():
                        count = len(data) if isinstance(data, list) else len(data.get("transactions", []))
                        result_counts["transactions"] += count
                    else:
                        result_counts["analyses"] += 1

                    self._log("FINCOSYS", f"Loaded: {filename}")
                except Exception as e:
                    self._log("FINCOSYS", f"Error loading {filename}: {e}")
        else:
            self._log("FINCOSYS", "FinCoSys exports directory not found")

        self.stage_status["load_financial_evidence"] = "completed"
        self.results["fincosys"] = result_counts
        self._log("FINCOSYS", f"Loaded {result_counts['files_loaded']} files")
        return result_counts

    def construct_hypergraph(self) -> Dict[str, Any]:
        """
        Construct the multi-repository hypergraph.

        Uses MultiRepoHypergraphConstructor from the hypergraph module.

        Returns:
            Hypergraph dictionary structure.
        """
        self._log("HYPERGRAPH", "Constructing multi-repository hypergraph...")
        self.stage_status["construct_hypergraph"] = "running"

        try:
            # Add LexRexHGNN src to path for imports
            lexrex_src = os.path.join(self.repo_paths["LexRexHGNN"], "src")
            if lexrex_src not in sys.path:
                sys.path.insert(0, lexrex_src)

            from hypergraph.constructor import (
                MultiRepoHypergraphConstructor,
                RepositoryConfig,
            )

            # Build repository configs
            repo_configs = [
                RepositoryConfig(
                    "cogpy", "revstream1", "Python",
                    "Revenue Stream case data models",
                    local_path=self.repo_paths.get("revstream1")
                ),
                RepositoryConfig(
                    "cogpy", "ad-res-j7", "JavaScript",
                    "Extended evidence repository",
                    local_path=self.repo_paths.get("ad-res-j7")
                ),
                RepositoryConfig(
                    "cogpy", "chainlex", "Scheme",
                    "ChainLex legal knowledge base",
                    local_path=self.repo_paths.get("chainlex")
                ),
                RepositoryConfig(
                    "cogpy", "fincosys", "Python",
                    "Financial analysis system",
                    local_path=self.repo_paths.get("fincosys")
                ),
            ]

            constructor = MultiRepoHypergraphConstructor(repositories=repo_configs)
            hypergraph = constructor.construct(
                workspace=self.workspace, skip_clone=True
            )

            self.stage_status["construct_hypergraph"] = "completed"
            self.results["hypergraph"] = {
                "nodes": hypergraph.get("unified_metrics", {}).get("total_nodes", 0),
                "edges": hypergraph.get("unified_metrics", {}).get("total_edges", 0),
                "cross_repo_nodes": hypergraph.get("unified_metrics", {}).get("cross_repo_nodes", 0),
            }
            self._log("HYPERGRAPH", f"Constructed hypergraph with "
                      f"{self.results['hypergraph']['nodes']} nodes, "
                      f"{self.results['hypergraph']['edges']} edges")
            return hypergraph

        except ImportError as e:
            self._log("HYPERGRAPH", f"Import error (running standalone?): {e}")
            self.stage_status["construct_hypergraph"] = "error"
            return {}
        except Exception as e:
            self._log("HYPERGRAPH", f"Construction error: {e}")
            self.stage_status["construct_hypergraph"] = "error"
            return {}

    def run_neuro_symbolic_analysis(
        self,
        entities_path: str,
        relations_path: str,
        events_path: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Run neuro-symbolic analysis using LexiCogFramework.

        Args:
            entities_path: Path to entities JSON file.
            relations_path: Path to relations JSON file.
            events_path: Optional path to events JSON file.

        Returns:
            Analysis results dictionary.
        """
        self._log("LEXICOG", "Running neuro-symbolic analysis...")
        self.stage_status["run_neuro_symbolic_analysis"] = "running"

        try:
            lexrex_src = os.path.join(self.repo_paths["LexRexHGNN"], "src")
            if lexrex_src not in sys.path:
                sys.path.insert(0, lexrex_src)

            from lexicog.integration import create_lexicog_framework

            framework = create_lexicog_framework()

            # Load data models
            counts = framework.load_data_models(
                entities_path, relations_path, events_path
            )
            self._log("LEXICOG", f"Loaded {counts['entities']} entities, "
                      f"{counts['relations']} relations, {counts['events']} events")

            # Create agent team
            agents = framework.create_agent_team()
            self._log("LEXICOG", f"Created agent team: {len(agents)} agents")

            # Generate case summary
            summary = framework.generate_case_summary()

            analysis_results = {
                "data_counts": counts,
                "agent_count": len(agents),
                "case_summary": summary,
            }

            self.stage_status["run_neuro_symbolic_analysis"] = "completed"
            self.results["lexicog"] = analysis_results
            self._log("LEXICOG", "Neuro-symbolic analysis complete")
            return analysis_results

        except ImportError as e:
            self._log("LEXICOG", f"Import error (running standalone?): {e}")
            self.stage_status["run_neuro_symbolic_analysis"] = "error"
            return {}
        except Exception as e:
            self._log("LEXICOG", f"Analysis error: {e}")
            self.stage_status["run_neuro_symbolic_analysis"] = "error"
            return {}

    def run_full_pipeline(self) -> Dict[str, Any]:
        """
        Run all pipeline stages in order.

        Returns:
            Comprehensive results dictionary with all stage outputs.
        """
        start_time = datetime.now()
        self._log("PIPELINE", "="*60)
        self._log("PIPELINE", "Starting full Legal Case Pipeline")
        self._log("PIPELINE", f"Case: {self.config.get('case', {}).get('number', 'Unknown')}")
        self._log("PIPELINE", "="*60)

        # Stage 1: Validate data contracts
        self._log("PIPELINE", "Stage 1/5: Validating data contracts")
        contracts_valid = self.validate_data_contracts()

        # Stage 2: Load ChainLex knowledge
        self._log("PIPELINE", "Stage 2/5: Loading ChainLex knowledge")
        chainlex_data = self.load_chainlex_knowledge()

        # Stage 3: Load financial evidence
        self._log("PIPELINE", "Stage 3/5: Loading financial evidence")
        financial_data = self.load_financial_evidence()

        # Stage 4: Construct hypergraph
        self._log("PIPELINE", "Stage 4/5: Constructing hypergraph")
        hypergraph = self.construct_hypergraph()

        # Stage 5: Run neuro-symbolic analysis
        self._log("PIPELINE", "Stage 5/5: Running neuro-symbolic analysis")
        revstream_path = self.repo_paths.get("revstream1", "")
        entities_path = os.path.join(
            revstream_path, "data_models", "entities", "entities.json"
        )
        relations_path = os.path.join(
            revstream_path, "data_models", "relations", "relations.json"
        )
        events_path = os.path.join(
            revstream_path, "data_models", "events", "events.json"
        )

        analysis = self.run_neuro_symbolic_analysis(
            entities_path, relations_path,
            events_path if os.path.exists(events_path) else None
        )

        # Compile final results
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        pipeline_results = {
            "pipeline": "LegalCasePipeline",
            "case": self.config.get("case", {}),
            "started": start_time.isoformat(),
            "completed": end_time.isoformat(),
            "duration_seconds": duration,
            "stage_status": dict(self.stage_status),
            "results": {
                "contracts_valid": contracts_valid,
                "chainlex": chainlex_data,
                "financial": financial_data,
                "hypergraph_summary": self.results.get("hypergraph", {}),
                "analysis": analysis,
            },
        }

        self._log("PIPELINE", "="*60)
        self._log("PIPELINE", f"Pipeline complete in {duration:.1f}s")
        self._log("PIPELINE", f"Stages: {len(self.stage_status)} executed")
        self._log("PIPELINE", "="*60)

        return pipeline_results

    def run_incremental(self, changed_repos: List[str]) -> Dict[str, Any]:
        """
        Run only the pipeline stages affected by changes in specific repos.

        Args:
            changed_repos: List of repository names that have changed.

        Returns:
            Results dictionary for the stages that were run.
        """
        self._log("PIPELINE", f"Incremental run for: {changed_repos}")
        incremental_results = {
            "mode": "incremental",
            "changed_repos": changed_repos,
            "stages_run": [],
        }

        # revstream1 changes affect contracts, hypergraph, and analysis
        if "revstream1" in changed_repos:
            self.validate_data_contracts()
            incremental_results["stages_run"].append("validate_data_contracts")

            self.construct_hypergraph()
            incremental_results["stages_run"].append("construct_hypergraph")

            revstream_path = self.repo_paths.get("revstream1", "")
            entities_path = os.path.join(
                revstream_path, "data_models", "entities", "entities.json"
            )
            relations_path = os.path.join(
                revstream_path, "data_models", "relations", "relations.json"
            )
            events_path = os.path.join(
                revstream_path, "data_models", "events", "events.json"
            )
            self.run_neuro_symbolic_analysis(
                entities_path, relations_path,
                events_path if os.path.exists(events_path) else None
            )
            incremental_results["stages_run"].append("run_neuro_symbolic_analysis")

        # chainlex changes affect knowledge loading and hypergraph
        if "chainlex" in changed_repos:
            self.load_chainlex_knowledge()
            incremental_results["stages_run"].append("load_chainlex_knowledge")

            if "construct_hypergraph" not in incremental_results["stages_run"]:
                self.construct_hypergraph()
                incremental_results["stages_run"].append("construct_hypergraph")

        # fincosys changes affect financial evidence and hypergraph
        if "fincosys" in changed_repos:
            self.load_financial_evidence()
            incremental_results["stages_run"].append("load_financial_evidence")

            if "construct_hypergraph" not in incremental_results["stages_run"]:
                self.construct_hypergraph()
                incremental_results["stages_run"].append("construct_hypergraph")

        # ad-res-j7 changes affect hypergraph
        if "ad-res-j7" in changed_repos:
            if "construct_hypergraph" not in incremental_results["stages_run"]:
                self.construct_hypergraph()
                incremental_results["stages_run"].append("construct_hypergraph")

        incremental_results["stage_status"] = dict(self.stage_status)
        incremental_results["results"] = dict(self.results)
        return incremental_results


def main():
    """Run the full legal case pipeline."""
    import argparse

    parser = argparse.ArgumentParser(
        description="LexRexHGNN Legal Case Pipeline Orchestrator"
    )
    parser.add_argument(
        "--workspace", default="/home/user",
        help="Root workspace directory containing all repositories"
    )
    parser.add_argument(
        "--config", default=None,
        help="Path to ecosystem.json configuration file"
    )
    parser.add_argument(
        "--incremental", nargs="*", default=None,
        help="Run incrementally for specified changed repos"
    )
    parser.add_argument(
        "--output", default=None,
        help="Output file for pipeline results JSON"
    )

    args = parser.parse_args()

    pipeline = LegalCasePipeline(
        workspace=args.workspace,
        config_path=args.config
    )

    if args.incremental is not None:
        results = pipeline.run_incremental(args.incremental)
    else:
        results = pipeline.run_full_pipeline()

    # Save results if output path specified
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"\nResults saved to: {args.output}")

    return results


if __name__ == "__main__":
    main()
