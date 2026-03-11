"""
Multi-Repository Synchronization Module
LexRexHGNN - Legal Hypergraph Neural Network

Handles synchronization of data models across repositories.
"""

import glob
import json
import os
import shutil
import subprocess
from datetime import datetime
from typing import Dict, List, Optional


class RepositorySynchronizer:
    """
    Synchronizes data models and filings across multiple repositories.
    
    Supports:
    - Entity/relation/event synchronization
    - Filing updates and versioning
    - GitHub Pages deployment
    - Commit batching (10 files per commit)
    """
    
    def __init__(self, workspace: str = "/home/ubuntu/repos"):
        self.workspace = workspace
        self.repositories = {
            "ad-res-j7": os.path.join(workspace, "ad-res-j7"),
            "revstream1": os.path.join(workspace, "revstream1"),
            "LexRexHGNN": os.path.join(workspace, "LexRexHGNN"),
            "chainlex": os.path.join(workspace, "chainlex"),
            "fincosys": os.path.join(workspace, "fincosys")
        }
        self.batch_size = 10
    
    def sync_all(self, commit_message: Optional[str] = None):
        """Synchronize all repositories."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = commit_message or f"LexRexHGNN sync: {timestamp}"
        
        for repo_name, repo_path in self.repositories.items():
            if os.path.exists(repo_path):
                self._sync_repository(repo_name, repo_path, message)
    
    def _sync_repository(self, name: str, path: str, message: str):
        """Sync a single repository."""
        print(f"[Sync] Synchronizing {name}...")
        
        os.chdir(path)
        
        # Stage all changes
        subprocess.run(["git", "add", "-A"], capture_output=True)
        
        # Check for changes
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True
        )
        
        if result.stdout.strip():
            # Commit changes
            subprocess.run(
                ["git", "commit", "-m", message],
                capture_output=True
            )
            
            # Push changes
            subprocess.run(["git", "push"], capture_output=True)
            print(f"[Sync] {name}: Changes pushed successfully")
        else:
            print(f"[Sync] {name}: No changes to sync")
    
    def sync_data_models(self, source_repo: str = "revstream1"):
        """
        Sync data models from source repository to LexRexHGNN.
        
        Args:
            source_repo: Source repository name
        """
        source_path = self.repositories.get(source_repo)
        target_path = self.repositories.get("LexRexHGNN")
        
        if not source_path or not target_path:
            print("[Sync] Error: Repository paths not found")
            return
        
        # Copy data models
        models = ["entities", "relations", "events", "timelines"]
        
        for model in models:
            source_file = os.path.join(
                source_path, "data_models", model, f"{model.rstrip('s')}.json"
            )
            if model == "entities":
                source_file = os.path.join(
                    source_path, "data_models", model, "entities.json"
                )
            elif model == "relations":
                source_file = os.path.join(
                    source_path, "data_models", model, "relations.json"
                )
            elif model == "timelines":
                source_file = os.path.join(
                    source_path, "data_models", model, "timeline.json"
                )
            
            if os.path.exists(source_file):
                target_dir = os.path.join(target_path, "data", model)
                os.makedirs(target_dir, exist_ok=True)
                
                # Read and copy
                with open(source_file, 'r') as f:
                    data = json.load(f)
                
                target_file = os.path.join(target_dir, os.path.basename(source_file))
                with open(target_file, 'w') as f:
                    json.dump(data, f, indent=2)
                
                print(f"[Sync] Copied {model} to LexRexHGNN")
    
    def update_filing(self, filing_type: str, content: str, repo: str = "revstream1"):
        """
        Update a legal filing in the repository.
        
        Args:
            filing_type: Type of filing (cipc, popia, npa_tax_fraud)
            content: Filing content
            repo: Target repository
        """
        repo_path = self.repositories.get(repo)
        if not repo_path:
            print(f"[Sync] Error: Repository {repo} not found")
            return
        
        date_str = datetime.now().strftime("%Y_%m_%d")
        filename_map = {
            "cipc": f"CIPC_COMPLAINT_REFINED_{date_str}.md",
            "popia": f"POPIA_COMPLAINT_REFINED_{date_str}.md",
            "npa_tax_fraud": f"NPA_TAX_FRAUD_REPORT_REFINED_{date_str}.md"
        }
        
        filename = filename_map.get(filing_type)
        if not filename:
            print(f"[Sync] Error: Unknown filing type {filing_type}")
            return
        
        # Write to docs/filings
        filings_dir = os.path.join(repo_path, "docs", "filings")
        os.makedirs(filings_dir, exist_ok=True)
        
        filepath = os.path.join(filings_dir, filename)
        with open(filepath, 'w') as f:
            f.write(content)
        
        print(f"[Sync] Updated filing: {filename}")
    
    def sync_data_targeted(self):
        """
        Targeted sync of data model files only (not entire repos).

        Copies:
        - revstream1/data_models/**/*.json -> LexRexHGNN/data/
        - chainlex/exports/*.json -> LexRexHGNN/data/chainlex/
        - fincosys/exports/*.json -> LexRexHGNN/data/fincosys/
        """
        target_base = os.path.join(self.repositories["LexRexHGNN"], "data")
        copied_files = []

        # 1. Copy revstream1/data_models/**/*.json -> LexRexHGNN/data/
        revstream_models = self.repositories.get("revstream1")
        if revstream_models and os.path.exists(revstream_models):
            data_models_dir = os.path.join(revstream_models, "data_models")
            if os.path.exists(data_models_dir):
                pattern = os.path.join(data_models_dir, "**", "*.json")
                for src_file in glob.glob(pattern, recursive=True):
                    # Preserve subdirectory structure under data_models/
                    rel_path = os.path.relpath(src_file, data_models_dir)
                    dest_file = os.path.join(target_base, rel_path)
                    os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                    shutil.copy2(src_file, dest_file)
                    copied_files.append(dest_file)
                    print(f"[Sync] Copied revstream1: {rel_path}")

        # 2. Copy chainlex/exports/*.json -> LexRexHGNN/data/chainlex/
        chainlex_path = self.repositories.get("chainlex")
        if chainlex_path and os.path.exists(chainlex_path):
            exports_dir = os.path.join(chainlex_path, "exports")
            if os.path.exists(exports_dir):
                dest_dir = os.path.join(target_base, "chainlex")
                os.makedirs(dest_dir, exist_ok=True)
                for src_file in glob.glob(os.path.join(exports_dir, "*.json")):
                    dest_file = os.path.join(dest_dir, os.path.basename(src_file))
                    shutil.copy2(src_file, dest_file)
                    copied_files.append(dest_file)
                    print(f"[Sync] Copied chainlex: {os.path.basename(src_file)}")

        # 3. Copy fincosys/exports/*.json -> LexRexHGNN/data/fincosys/
        fincosys_path = self.repositories.get("fincosys")
        if fincosys_path and os.path.exists(fincosys_path):
            exports_dir = os.path.join(fincosys_path, "exports")
            if os.path.exists(exports_dir):
                dest_dir = os.path.join(target_base, "fincosys")
                os.makedirs(dest_dir, exist_ok=True)
                for src_file in glob.glob(os.path.join(exports_dir, "*.json")):
                    dest_file = os.path.join(dest_dir, os.path.basename(src_file))
                    shutil.copy2(src_file, dest_file)
                    copied_files.append(dest_file)
                    print(f"[Sync] Copied fincosys: {os.path.basename(src_file)}")

        print(f"[Sync] Targeted sync complete: {len(copied_files)} files copied")
        return copied_files

    def update_sync_manifest(self):
        """
        Write a sync_manifest.json tracking versions and timestamps
        for all synchronized data.
        """
        lexrex_path = self.repositories.get("LexRexHGNN")
        if not lexrex_path:
            print("[Sync] Error: LexRexHGNN path not found")
            return

        manifest = {
            "last_sync": datetime.now().isoformat(),
            "sync_tool": "RepositorySynchronizer",
            "repositories": {}
        }

        for name, path in self.repositories.items():
            repo_info = {
                "path": path,
                "exists": os.path.exists(path)
            }

            if os.path.exists(path):
                # Try to get git commit hash
                try:
                    result = subprocess.run(
                        ["git", "log", "-1", "--format=%H"],
                        capture_output=True, text=True,
                        cwd=path
                    )
                    if result.returncode == 0:
                        repo_info["last_commit"] = result.stdout.strip()
                except Exception:
                    pass

                # Try to get version from data models
                version_file = os.path.join(path, "data_models", "version.json")
                if os.path.exists(version_file):
                    try:
                        with open(version_file, 'r') as f:
                            repo_info["data_version"] = json.load(f)
                    except Exception:
                        pass

            manifest["repositories"][name] = repo_info

        # Write manifest
        manifest_path = os.path.join(lexrex_path, "sync_manifest.json")
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)

        print(f"[Sync] Manifest written to: {manifest_path}")
        return manifest_path

    def get_sync_status(self) -> Dict:
        """Get synchronization status for all repositories."""
        status = {}
        
        for name, path in self.repositories.items():
            if os.path.exists(path):
                os.chdir(path)
                
                # Get last commit
                result = subprocess.run(
                    ["git", "log", "-1", "--format=%H %s"],
                    capture_output=True, text=True
                )
                
                # Get status
                status_result = subprocess.run(
                    ["git", "status", "--porcelain"],
                    capture_output=True, text=True
                )
                
                status[name] = {
                    "path": path,
                    "last_commit": result.stdout.strip(),
                    "has_changes": bool(status_result.stdout.strip()),
                    "changes_count": len(status_result.stdout.strip().split('\n')) if status_result.stdout.strip() else 0
                }
            else:
                status[name] = {"path": path, "exists": False}
        
        return status


if __name__ == "__main__":
    sync = RepositorySynchronizer()
    
    # Print status
    status = sync.get_sync_status()
    print("\nRepository Sync Status:")
    print("="*60)
    for name, info in status.items():
        print(f"\n{name}:")
        for key, value in info.items():
            print(f"  {key}: {value}")
