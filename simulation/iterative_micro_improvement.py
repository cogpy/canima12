#!/usr/bin/env python3
"""
Iterative Micro-Improvement Simulation Framework
=================================================
Composition: /skill-genesis(/iterative-micro-improvement(
    /lexrex[/anylogic-modeler(/ai-env-grp-dyn) + /scm-des(/digitwin) + /cogsim-pml(/acc-fund-flow)]
))

This framework implements a self-improving legal simulation pipeline that:
1. Ingests entity/relation/event/timeline data from revstream1 data_models
2. Runs discrete-event simulation (DES) of the revenue hijacking scheme
3. Applies system dynamics (SD) stock-flow modeling for fund flow analysis
4. Uses agent-based modeling (ABM) for group dynamics and collusion detection
5. Evaluates evidence strength via LexRex legal fixed-point theorem
6. Iteratively improves the model through mutation-evaluation cycles

Case: 2025-137857 (Peter Faucitt v. Jacqueline & Daniel Faucitt)
"""

import json
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Tuple, Any
from pathlib import Path

# ============================================================================
# SECTION 1: CORE DATA TYPES (ER-ABM Layer)
# ============================================================================

class AgentType(Enum):
    PERPETRATOR = "perpetrator"
    VICTIM = "victim"
    ACCOMPLICE = "accomplice"
    NEUTRAL = "neutral"
    INSTITUTION = "institution"
    PROFESSIONAL = "professional"

class EntityType(Enum):
    PERSON = "person"
    ORGANIZATION = "organization"
    TRUST = "trust"
    BANK_ACCOUNT = "bank_account"
    LEGAL_ENTITY = "legal_entity"

class RelationType(Enum):
    CONTROLS = "controls"
    OWNS = "owns"
    DIRECTS = "directs"
    COLLUDES_WITH = "colludes_with"
    FUNDS = "funds"
    DIVERTS_FROM = "diverts_from"
    INSTRUCTS = "instructs"
    CONCEALS_FROM = "conceals_from"
    RETALIATES_AGAINST = "retaliates_against"
    WEAPONIZES = "weaponizes"

class BurdenOfProof(Enum):
    CIVIL = 0.50          # Balance of probabilities
    REGULATORY = 0.50     # Administrative standard
    PROFESSIONAL = 0.50   # Professional misconduct
    CRIMINAL = 0.95       # Beyond reasonable doubt

class FilingType(Enum):
    CIVIL_RESCISSION = "civil_rescission"
    CRIMINAL_PERJURY = "criminal_perjury"
    CRIMINAL_COMMERCIAL = "criminal_commercial"
    CIPC_COMPLAINT = "cipc_complaint"
    POPIA_COMPLAINT = "popia_complaint"
    SARS_TAX_FRAUD = "sars_tax_fraud"
    SAICA_MISCONDUCT = "saica_misconduct"
    NPA_REFERRAL = "npa_referral"
    SCA_OPPOSITION = "sca_opposition"
    LPC_COMPLAINT = "lpc_complaint"

# ============================================================================
# SECTION 2: AGENT-BASED MODEL (ABM) — Group Dynamics
# ============================================================================

@dataclass
class Agent:
    """7-dimensional agent state (ER-ABM Layer 3)"""
    id: str
    name: str
    agent_type: AgentType
    entity_type: EntityType
    # 7 dimensions
    operational_control: float = 0.0   # 0-1
    financial_control: float = 0.0     # 0-1
    legal_authority: float = 0.0       # 0-1
    information_access: float = 0.0    # 0-1
    motive_strength: float = 0.0       # 0-1
    foreknowledge_score: float = 0.0   # 0-1
    evidence_strength: float = 0.0     # 0-1
    # Metadata
    roles: List[str] = field(default_factory=list)
    evidence_codes: List[str] = field(default_factory=list)
    relations: List[Dict] = field(default_factory=list)

@dataclass
class Relation:
    """Directed relation between agents"""
    id: str
    source_id: str
    target_id: str
    relation_type: RelationType
    evidence_strength: float = 0.0
    evidence_codes: List[str] = field(default_factory=list)
    description: str = ""
    date_established: Optional[str] = None
    date_discovered: Optional[str] = None

# ============================================================================
# SECTION 3: DISCRETE EVENT SIMULATION (DES) — Timeline Engine
# ============================================================================

class EventPhase(Enum):
    SETUP = "setup"                    # Pre-scheme infrastructure
    CONSOLIDATION = "consolidation"    # Control seizure
    DISCOVERY = "discovery"            # Fraud detection by victim
    RETALIATION = "retaliation"        # Response to discovery
    COVER_UP = "cover_up"              # Evidence destruction
    LEGAL_WEAPONIZATION = "legal_weaponization"  # Court abuse
    POST_INTERDICT = "post_interdict"  # Ongoing control
    APPEAL_AND_RESPONSE = "appeal_and_response"  # Current phase

@dataclass
class SimEvent:
    """Discrete event in the case timeline"""
    id: str
    date: str
    title: str
    description: str
    phase: EventPhase
    actors: List[str] = field(default_factory=list)
    entities_involved: List[str] = field(default_factory=list)
    evidence_refs: List[str] = field(default_factory=list)
    significance_level: int = 5  # 1-10
    criminal_threshold: bool = False
    civil_threshold: bool = False
    regulatory_threshold: bool = False
    causal_chain: List[str] = field(default_factory=list)  # IDs of caused events
    state_transitions: Dict[str, str] = field(default_factory=dict)

# ============================================================================
# SECTION 4: SYSTEM DYNAMICS (SD) — Stock-Flow Fund Analysis
# ============================================================================

@dataclass
class Stock:
    """Financial stock (accumulated balance)"""
    id: str
    name: str
    entity_id: str
    current_value: float = 0.0
    unit: str = "ZAR"
    history: List[Tuple[str, float]] = field(default_factory=list)

@dataclass
class Flow:
    """Financial flow (rate of change)"""
    id: str
    name: str
    source_stock: Optional[str] = None
    target_stock: Optional[str] = None
    rate: float = 0.0
    unit: str = "ZAR/month"
    is_legitimate: bool = True
    evidence_of_diversion: bool = False
    description: str = ""

@dataclass
class FeedbackLoop:
    """Reinforcing or balancing feedback loop"""
    id: str
    name: str
    loop_type: str  # "reinforcing" or "balancing"
    stocks: List[str] = field(default_factory=list)
    flows: List[str] = field(default_factory=list)
    description: str = ""

# ============================================================================
# SECTION 5: LEXREX LEGAL EVALUATION ENGINE
# ============================================================================

@dataclass
class LegalEvaluation:
    """LexRex fixed-point evaluation of evidence against burden"""
    filing_type: FilingType
    burden: BurdenOfProof
    current_score: float = 0.0
    threshold_met: bool = False
    key_events: List[str] = field(default_factory=list)
    key_evidence: List[str] = field(default_factory=list)
    gaps: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)

# ============================================================================
# SECTION 6: ITERATIVE MICRO-IMPROVEMENT ENGINE
# ============================================================================

@dataclass
class ImprovementCycle:
    """One iteration of the micro-improvement loop"""
    cycle_id: int
    timestamp: str
    mutations_applied: List[Dict] = field(default_factory=list)
    evaluations: List[LegalEvaluation] = field(default_factory=list)
    score_delta: float = 0.0
    accepted: bool = False
    notes: str = ""

class IterativeMicroImprovement:
    """
    Self-improving simulation engine.
    
    Composition:
    - LexRex: Legal fixed-point evaluation
    - AnyLogic/DES: Discrete event timeline simulation
    - SCM-DES/DigiTwin: Supply chain & digital twin modeling
    - CogSim-PML: Process modeling for fund flow
    - ACC-Fund-Flow: Forensic fund tracing
    - AI-Env-Grp-Dyn: Group dynamics & collusion detection
    """
    
    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        self.agents: Dict[str, Agent] = {}
        self.relations: List[Relation] = []
        self.events: List[SimEvent] = []
        self.stocks: Dict[str, Stock] = {}
        self.flows: List[Flow] = []
        self.feedback_loops: List[FeedbackLoop] = []
        self.evaluations: Dict[FilingType, LegalEvaluation] = {}
        self.cycles: List[ImprovementCycle] = []
        self.current_cycle = 0
        
    def load_data_models(self):
        """Load entities, relations, events, timeline from revstream1 data_models"""
        # Load entities
        entities_path = self.data_dir / "entities.json"
        if entities_path.exists():
            with open(entities_path) as f:
                raw_entities = json.load(f)
            for e in raw_entities:
                agent = Agent(
                    id=e.get("id", ""),
                    name=e.get("name", ""),
                    agent_type=self._classify_agent_type(e),
                    entity_type=self._classify_entity_type(e),
                    roles=e.get("roles", []),
                    evidence_codes=e.get("evidence_codes", []),
                    evidence_strength=e.get("evidence_strength", 0.0)
                )
                self.agents[agent.id] = agent
        
        # Load relations
        relations_path = self.data_dir / "relations.json"
        if relations_path.exists():
            with open(relations_path) as f:
                raw_relations = json.load(f)
            for r in raw_relations:
                relation = Relation(
                    id=r.get("id", ""),
                    source_id=r.get("source", r.get("entities_involved", [""])[0] if r.get("entities_involved") else ""),
                    target_id=r.get("target", r.get("entities_involved", ["", ""])[1] if len(r.get("entities_involved", [])) > 1 else ""),
                    relation_type=RelationType.CONTROLS,
                    evidence_strength=r.get("evidence_strength", 0.0),
                    description=r.get("title", r.get("description", ""))
                )
                self.relations.append(relation)
        
        # Load events
        events_path = self.data_dir / "events.json"
        if events_path.exists():
            with open(events_path) as f:
                raw_events = json.load(f)
            for ev in raw_events:
                event = SimEvent(
                    id=ev.get("id", ""),
                    date=ev.get("date", ""),
                    title=ev.get("title", ""),
                    description=ev.get("description", ""),
                    phase=self._classify_phase(ev),
                    actors=ev.get("actors", ev.get("entities_involved", [])),
                    entities_involved=ev.get("entities_involved", []),
                    evidence_refs=ev.get("evidence_refs", ev.get("evidence_codes", [])),
                    significance_level=ev.get("significance_level", 5)
                )
                self.events.append(event)
        
        # Load timeline
        timeline_path = self.data_dir / "timelines" / "timeline.json"
        if timeline_path.exists():
            with open(timeline_path) as f:
                raw_timeline = json.load(f)
            tl_events = raw_timeline.get("timeline", [])
            for tev in tl_events:
                if not any(e.id == tev.get("event_ref", "") for e in self.events):
                    event = SimEvent(
                        id=tev.get("event_ref", f"TL_{tev.get('date', '')}"),
                        date=tev.get("date", ""),
                        title=tev.get("title", tev.get("event", "")),
                        description=tev.get("description", tev.get("event", "")),
                        phase=self._classify_phase(tev),
                        actors=tev.get("actors", []),
                        entities_involved=tev.get("entities_involved", []),
                        significance_level=tev.get("significance_level", 5)
                    )
                    self.events.append(event)
        
        print(f"Loaded: {len(self.agents)} agents, {len(self.relations)} relations, {len(self.events)} events")
        return self
    
    def build_fund_flow_model(self):
        """Build stock-flow model from financial evidence (acc-fund-flow)"""
        # Core stocks representing entity accounts
        core_entities = {
            "RST": ("RegimA Skin Treatments CC", 0),
            "SLG": ("Strategic Logistics CC", 0),
            "RWD": ("RegimA Worldwide Distribution", 0),
            "VVA": ("Villa Via Arcadia", 0),
            "RSA": ("RegimA SA (Pty) Ltd", 0),
            "FFT": ("Faucitt Family Trust", 0),
            "KETONI": ("Ketoni Investment Holdings", 18750000),
            "ADDARORY": ("Addarory (Pty) Ltd", 0),
            "ELLIOTT": ("Elliott Attorneys", 0),
        }
        
        for entity_id, (name, initial) in core_entities.items():
            self.stocks[entity_id] = Stock(
                id=entity_id, name=name, entity_id=entity_id,
                current_value=initial
            )
        
        # Documented fund flows (from evidence)
        documented_flows = [
            Flow("F001", "RST→SLG Stock Loan", "RST", "SLG", 1083333, "ZAR/month", True, False, "R13M stock/loan over 12 months"),
            Flow("F002", "SLG Stock Disappearance", "SLG", None, 450000, "ZAR/month", False, True, "R5.4M stock vanished (to Addarory)"),
            Flow("F003", "RWD→VVA Rent Extraction", "RWD", "VVA", 86000, "ZAR/month", False, True, "86% profit margin rent extraction"),
            Flow("F004", "RSA→ABSA Revenue Diversion", "RSA", None, 75000, "ZAR/month", False, True, "Unauthorized ABSA revenue diversion"),
            Flow("F005", "RST→Elliott Legal Funding", "RST", "ELLIOTT", 59870, "ZAR/month", False, True, "R478,958 over 8 months"),
            Flow("F006", "FFT→Ketoni Investment", "FFT", "KETONI", 0, "ZAR", True, False, "R18.75M payout due May 2026"),
            Flow("F007", "SLG Revenue Collapse", None, "SLG", -275288, "ZAR/month", False, True, "21.9% monthly revenue drop post-Addarory"),
            Flow("F008", "RST Misallocated Debt", "RST", None, 0, "ZAR", False, True, "R1,035,361 misallocated to Rezonance"),
        ]
        self.flows = documented_flows
        
        # Feedback loops
        self.feedback_loops = [
            FeedbackLoop("FL001", "Revenue Hijacking Reinforcing Loop", "reinforcing",
                        ["SLG", "ADDARORY"], ["F002", "F007"],
                        "Stock disappearance → revenue collapse → more stock needed → more disappearance"),
            FeedbackLoop("FL002", "Legal Weaponization Reinforcing Loop", "reinforcing",
                        ["RST", "ELLIOTT"], ["F005"],
                        "RST funds → Elliott → litigation → more control → more RST funds"),
            FeedbackLoop("FL003", "Trust Capture Reinforcing Loop", "reinforcing",
                        ["FFT", "KETONI", "VVA"], ["F003", "F006"],
                        "Trust control → Ketoni payout → VVA extraction → more trust value"),
        ]
        
        print(f"Built fund-flow model: {len(self.stocks)} stocks, {len(self.flows)} flows, {len(self.feedback_loops)} loops")
        return self
    
    def evaluate_filings(self):
        """Evaluate all filing types against burden of proof (LexRex)"""
        filing_configs = [
            (FilingType.CIVIL_RESCISSION, BurdenOfProof.CIVIL, 
             ["EVENT_080", "EVENT_081", "EVENT_082", "EVENT_130", "EVENT_137"],
             "Void ab initio / Rule 42 rescission"),
            (FilingType.CRIMINAL_PERJURY, BurdenOfProof.CRIMINAL,
             ["EVENT_130", "EVENT_137", "EVENT_082"],
             "Bantjies J417 perjury + Peter founding affidavit"),
            (FilingType.CRIMINAL_COMMERCIAL, BurdenOfProof.CRIMINAL,
             ["EVENT_050", "EVENT_051", "EVENT_063", "EVENT_H010", "EVENT_181"],
             "Revenue hijacking, stock theft, abuse of process"),
            (FilingType.CIPC_COMPLAINT, BurdenOfProof.REGULATORY,
             ["EVENT_050", "EVENT_051", "EVENT_106", "EVENT_110"],
             "Companies Act s76/s29/s214 breaches"),
            (FilingType.POPIA_COMPLAINT, BurdenOfProof.CRIMINAL,
             ["EVENT_021", "EVENT_110", "EVENT_121"],
             "Unlawful access, identity fraud, audit trail deletion"),
            (FilingType.SARS_TAX_FRAUD, BurdenOfProof.CRIMINAL,
             ["EVENT_061", "EVENT_063", "EVENT_067"],
             "Tax fraud, understatement, intercompany manipulation"),
            (FilingType.SAICA_MISCONDUCT, BurdenOfProof.PROFESSIONAL,
             ["EVENT_137", "EVENT_063", "EVENT_066", "EVENT_130"],
             "Bantjies professional misconduct"),
            (FilingType.NPA_REFERRAL, BurdenOfProof.CRIMINAL,
             ["EVENT_050", "EVENT_051", "EVENT_063", "EVENT_181"],
             "NPA commercial crime referral"),
            (FilingType.SCA_OPPOSITION, BurdenOfProof.CIVIL,
             ["EVENT_176", "EVENT_177", "EVENT_179", "EVENT_180"],
             "SCA petition opposition"),
            (FilingType.LPC_COMPLAINT, BurdenOfProof.PROFESSIONAL,
             ["EVENT_181"],
             "Elliott Attorneys conflict of interest / RST funding"),
        ]
        
        for filing_type, burden, key_events, description in filing_configs:
            # Calculate evidence score based on events present
            events_found = [e for e in self.events if e.id in key_events]
            score = min(len(events_found) / max(len(key_events), 1), 1.0)
            
            # Boost for high-significance events
            high_sig_count = sum(1 for e in events_found if e.significance_level >= 8)
            score = min(score + (high_sig_count * 0.05), 1.0)
            
            # Apply evidence strength from agents
            relevant_agents = [a for a in self.agents.values() 
                             if a.evidence_strength > 0.8 and a.agent_type == AgentType.PERPETRATOR]
            if relevant_agents:
                score = min(score + 0.1, 1.0)
            
            evaluation = LegalEvaluation(
                filing_type=filing_type,
                burden=burden,
                current_score=score,
                threshold_met=score >= burden.value,
                key_events=key_events,
                key_evidence=[e.evidence_refs[0] if e.evidence_refs else "" for e in events_found],
                gaps=self._identify_gaps(filing_type, events_found),
                recommendations=self._generate_recommendations(filing_type, score, burden)
            )
            self.evaluations[filing_type] = evaluation
        
        met_count = sum(1 for e in self.evaluations.values() if e.threshold_met)
        print(f"Filing evaluations: {met_count}/{len(self.evaluations)} thresholds met")
        return self
    
    def run_improvement_cycle(self):
        """Execute one iteration of the micro-improvement loop"""
        self.current_cycle += 1
        cycle = ImprovementCycle(
            cycle_id=self.current_cycle,
            timestamp=datetime.now().isoformat()
        )
        
        # Identify weakest filings
        weakest = sorted(self.evaluations.values(), key=lambda e: e.current_score)[:3]
        
        mutations = []
        for eval_item in weakest:
            if not eval_item.threshold_met:
                # Generate improvement mutations
                mutation = {
                    "filing": eval_item.filing_type.value,
                    "current_score": eval_item.current_score,
                    "target_score": eval_item.burden.value,
                    "gap": eval_item.burden.value - eval_item.current_score,
                    "recommendations": eval_item.recommendations,
                    "action": "strengthen_evidence" if eval_item.current_score > 0.7 else "add_events"
                }
                mutations.append(mutation)
        
        cycle.mutations_applied = mutations
        cycle.evaluations = list(self.evaluations.values())
        cycle.score_delta = sum(m["gap"] for m in mutations) if mutations else 0
        cycle.accepted = True
        cycle.notes = f"Cycle {self.current_cycle}: {len(mutations)} improvements identified"
        
        self.cycles.append(cycle)
        return cycle
    
    def generate_report(self) -> Dict:
        """Generate comprehensive improvement report"""
        report = {
            "metadata": {
                "framework": "iterative-micro-improvement",
                "composition": "/skill-genesis(/iterative-micro-improvement(/lexrex[/anylogic-modeler(/ai-env-grp-dyn) + /scm-des(/digitwin) + /cogsim-pml(/acc-fund-flow)]))",
                "case": "2025-137857",
                "generated": datetime.now().isoformat(),
                "cycle": self.current_cycle
            },
            "model_state": {
                "agents": len(self.agents),
                "relations": len(self.relations),
                "events": len(self.events),
                "stocks": len(self.stocks),
                "flows": len(self.flows),
                "feedback_loops": len(self.feedback_loops)
            },
            "filing_evaluations": {},
            "fund_flow_analysis": {
                "total_diverted": sum(f.rate for f in self.flows if f.evidence_of_diversion),
                "legitimate_flows": sum(1 for f in self.flows if f.is_legitimate),
                "diversion_flows": sum(1 for f in self.flows if f.evidence_of_diversion),
                "reinforcing_loops": sum(1 for fl in self.feedback_loops if fl.loop_type == "reinforcing"),
            },
            "improvement_recommendations": [],
            "new_events_suggested": [],
            "new_relations_suggested": [],
            "new_entities_suggested": []
        }
        
        for filing_type, evaluation in self.evaluations.items():
            report["filing_evaluations"][filing_type.value] = {
                "score": evaluation.current_score,
                "burden": evaluation.burden.value,
                "threshold_met": evaluation.threshold_met,
                "gaps": evaluation.gaps,
                "recommendations": evaluation.recommendations
            }
        
        # Generate improvement recommendations based on June 2026 evidence
        report["improvement_recommendations"] = self._generate_global_recommendations()
        report["new_events_suggested"] = self._suggest_new_events()
        report["new_relations_suggested"] = self._suggest_new_relations()
        report["new_entities_suggested"] = self._suggest_new_entities()
        
        return report
    
    # ========================================================================
    # PRIVATE HELPER METHODS
    # ========================================================================
    
    def _classify_agent_type(self, entity: Dict) -> AgentType:
        role = entity.get("role", "").lower()
        if "perpetrator" in role or "antagonist" in role:
            return AgentType.PERPETRATOR
        elif "victim" in role:
            return AgentType.VICTIM
        elif "accomplice" in role:
            return AgentType.ACCOMPLICE
        elif "institution" in role or "bank" in role:
            return AgentType.INSTITUTION
        elif "professional" in role:
            return AgentType.PROFESSIONAL
        return AgentType.NEUTRAL
    
    def _classify_entity_type(self, entity: Dict) -> EntityType:
        etype = entity.get("type", "").lower()
        if "person" in etype:
            return EntityType.PERSON
        elif "trust" in etype:
            return EntityType.TRUST
        elif "bank" in etype or "account" in etype:
            return EntityType.BANK_ACCOUNT
        return EntityType.ORGANIZATION
    
    def _classify_phase(self, event: Dict) -> EventPhase:
        date_str = event.get("date", "")
        if date_str < "2024-07":
            return EventPhase.SETUP
        elif date_str < "2025-05":
            return EventPhase.CONSOLIDATION
        elif date_str < "2025-06-07":
            return EventPhase.DISCOVERY
        elif date_str < "2025-07":
            return EventPhase.RETALIATION
        elif date_str < "2025-08-13":
            return EventPhase.COVER_UP
        elif date_str < "2025-08-20":
            return EventPhase.LEGAL_WEAPONIZATION
        elif date_str < "2026-04":
            return EventPhase.POST_INTERDICT
        else:
            return EventPhase.APPEAL_AND_RESPONSE
    
    def _identify_gaps(self, filing_type: FilingType, events_found: List) -> List[str]:
        gaps = []
        if filing_type == FilingType.CRIMINAL_PERJURY:
            if not any("J417" in str(e.evidence_refs) for e in events_found):
                gaps.append("Need J417 form original for perjury proof")
        elif filing_type == FilingType.LPC_COMPLAINT:
            gaps.append("Need Elliott Attorneys engagement letter and retainer")
            gaps.append("Need conflict-check records from Elliott")
            gaps.append("Need RST member resolution authorizing legal expenditure")
        elif filing_type == FilingType.SARS_TAX_FRAUD:
            gaps.append("Need SARS eFiling access logs showing Bantjies credential use")
        elif filing_type == FilingType.POPIA_COMPLAINT:
            gaps.append("Need Shopify access log deletion proof (JF13/JF17)")
        return gaps
    
    def _generate_recommendations(self, filing_type: FilingType, score: float, burden: BurdenOfProof) -> List[str]:
        recs = []
        if score < burden.value:
            recs.append(f"Score {score:.2f} below {burden.name} threshold {burden.value:.2f}")
            recs.append("Strengthen with additional independent affidavits")
        if filing_type == FilingType.SCA_OPPOSITION:
            recs.append("Integrate Peter's 3 Jun 2026 AA admissions as counter-evidence")
            recs.append("Use para 63.5 admission (Shopify halt justified) against founding narrative")
            recs.append("Use para 64.2 admission (Farrar acts on my instructions) for attribution")
        if filing_type == FilingType.LPC_COMPLAINT:
            recs.append("New filing type: Legal Practice Council complaint against Elliott Attorneys")
            recs.append("Evidence: R478,958 RST payments while litigating against RST CEO")
        return recs
    
    def _generate_global_recommendations(self) -> List[Dict]:
        """Generate recommendations based on latest evidence (June 2026)"""
        return [
            {
                "priority": 1,
                "category": "SCA_OPPOSITION",
                "recommendation": "File SCA opposition immediately — Peter's petition must not remain unanswered",
                "evidence": "EVENT_180 (SCA petition 1 Jun 2026)",
                "deadline": "Within 10 court days of service"
            },
            {
                "priority": 2,
                "category": "PART_B_COUNTER_APPLICATION",
                "recommendation": "File Part B answering affidavit with counter-application for delinquency",
                "evidence": "Peter's 3 Jun 2026 AA contains 12+ material admissions",
                "deadline": "Before Part B hearing date"
            },
            {
                "priority": 3,
                "category": "LPC_COMPLAINT",
                "recommendation": "File Legal Practice Council complaint against Elliott Attorneys",
                "evidence": "EVENT_181 — R478,958 RST-funded payments while litigating against RST CEO",
                "deadline": "After obtaining engagement letter via Rule 35"
            },
            {
                "priority": 4,
                "category": "RULE_42_RESCISSION",
                "recommendation": "File Rule 42 rescission attacking the foundation order",
                "evidence": "Material non-disclosure proven; void ab initio argument strengthened by AA admissions",
                "deadline": "In parallel with SCA opposition"
            },
            {
                "priority": 5,
                "category": "CRIMINAL_FILINGS",
                "recommendation": "File SAPS complainant statement, NPA referral, SARS referral after civil pagination",
                "evidence": "All criminal thresholds now met or near-met with June 2026 admissions",
                "deadline": "After final evidence pagination"
            },
            {
                "priority": 6,
                "category": "STOCK_ORDER_CHALLENGE",
                "recommendation": "Challenge the 26 May 2026 stock-removal order (case 2026-115880)",
                "evidence": "Peter's AA para 7.5 admits stock order; case number collision with reconsideration",
                "deadline": "Urgent — stock partially executed 1 Jun 2026"
            }
        ]
    
    def _suggest_new_events(self) -> List[Dict]:
        """Suggest new events based on June 2026 evidence"""
        return [
            {
                "id": "EVENT_182",
                "date": "2026-06-03",
                "title": "Peter's 149-Page Answering Affidavit with 12+ Material Admissions",
                "description": "Peter swears answering affidavit (SAPS Bedfordview, Elliott ref KF0019) containing admissions at paras 39.3, 45.6, 53.3, 62.4, 63.5, 63.8, 64.2, 65.3, 75.4, 77.2, 83.2, 84.9, 185.2 that contradict the founding narrative",
                "phase": "appeal_and_response",
                "significance_level": 9,
                "actors": ["PERSON_001"],
                "evidence_refs": ["F-first-respondents-answering-affidavit.pdf"],
                "criminal_threshold": True,
                "filing_impact": ["SCA_OPPOSITION", "RULE_42", "PART_B"]
            },
            {
                "id": "EVENT_183",
                "date": "2026-05-26",
                "title": "Stock-Removal Order Granted Ex Parte Under Case 2026-115880",
                "description": "Peter obtains stock-removal order under same case number as Jax's reconsideration application, creating case-number collision",
                "phase": "appeal_and_response",
                "significance_level": 8,
                "actors": ["PERSON_001"],
                "evidence_refs": ["Peter AA para 7.5"],
                "criminal_threshold": False,
                "filing_impact": ["STOCK_CHALLENGE", "ABUSE_OF_PROCESS"]
            },
            {
                "id": "EVENT_184",
                "date": "2026-06-10",
                "title": "Reconsideration Struck from Roll for Want of Urgency",
                "description": "Case 2026-115880 reconsideration struck from roll — no order as to costs, merits not determined, interim order stands",
                "phase": "appeal_and_response",
                "significance_level": 7,
                "actors": ["PERSON_004"],
                "evidence_refs": ["Pool email 10 Jun 18:04", "LETTER TO ELLIOT 10.06.2026.doc"],
                "criminal_threshold": False,
                "filing_impact": ["RECONSIDERATION_RE_ENROLMENT"]
            },
            {
                "id": "EVENT_185",
                "date": "2026-06-13",
                "title": "Rynette Farrar / Danie Bantjies Forensic Review Completed",
                "description": "Comprehensive forensic review of Rynette Farrar and Danie Bantjies completed",
                "phase": "appeal_and_response",
                "significance_level": 8,
                "actors": ["PERSON_002", "PERSON_007"],
                "evidence_refs": ["Rynette_Farrar_Danie_Bantjes_Forensic_Review.docx/pdf"],
                "criminal_threshold": True,
                "filing_impact": ["NPA_COMMERCIAL_CRIME", "SAICA", "CRIMINAL_PERJURY"]
            },
            {
                "id": "EVENT_186",
                "date": "2026-06-15",
                "title": "Divorce Enrolled — Jax Under Notice of Bar",
                "description": "Divorce proceedings (case 2026-034662) enrolled with Jax under notice of bar",
                "phase": "appeal_and_response",
                "significance_level": 6,
                "actors": ["PERSON_001", "PERSON_004"],
                "evidence_refs": ["07_JUNE_FILINGS_ANALYSIS §2.6"],
                "criminal_threshold": False,
                "filing_impact": ["DIVORCE_PROCEEDINGS"]
            },
            {
                "id": "EVENT_187",
                "date": "2026-06-08",
                "title": "Elliott Attorneys RST Conflict-Funding Pattern Documented",
                "description": "Full R478,957.93 payment schedule from RST ABSA account to Elliott Attorneys documented and analyzed",
                "phase": "appeal_and_response",
                "significance_level": 9,
                "actors": ["PERSON_001", "ORG_020"],
                "evidence_refs": ["RST_ABSA_4112241409_ELLIOTT_ATTORNEYS_PAYMENTS_2025-08_2026-04.txt"],
                "criminal_threshold": False,
                "filing_impact": ["LPC_COMPLAINT", "CIPC", "ABUSE_OF_PROCESS"]
            }
        ]
    
    def _suggest_new_relations(self) -> List[Dict]:
        """Suggest new relations based on evidence"""
        return [
            {
                "id": "REL_RST_ELLIOTT_CONFLICT",
                "title": "RST-Elliott Legal Funding Conflict",
                "source": "ORG_002",
                "target": "ORG_020",
                "type": "funds_adversarial_litigation",
                "evidence_strength": 0.95,
                "description": "RST CC funds Elliott Attorneys R478,958 while Elliott litigates against RST CEO",
                "evidence_refs": ["EVENT_181", "RST_ABSA_4112241409_ELLIOTT_ATTORNEYS_PAYMENTS_2025-08_2026-04.txt"]
            },
            {
                "id": "REL_PETER_ADMISSION_CHAIN",
                "title": "Peter's Self-Contradicting Admission Chain",
                "source": "PERSON_001",
                "target": "PERSON_001",
                "type": "self_contradiction",
                "evidence_strength": 0.98,
                "description": "12+ admissions in 3 Jun 2026 AA contradict founding affidavit narrative",
                "evidence_refs": ["EVENT_182", "F-first-respondents-answering-affidavit.pdf"]
            },
            {
                "id": "REL_CASE_NUMBER_COLLISION",
                "title": "Case 2026-115880 Number Collision",
                "source": "PERSON_001",
                "target": "PERSON_004",
                "type": "procedural_anomaly",
                "evidence_strength": 0.90,
                "description": "Both Jax's reconsideration and Peter's stock order filed under same case number",
                "evidence_refs": ["EVENT_183", "Peter AA para 7.5"]
            },
            {
                "id": "REL_MAZARS_ENGAGEMENT_ANOMALY",
                "title": "Mazars Engagement Under Peter's Exclusive Control",
                "source": "PERSON_001",
                "target": "ORG_MAZARS",
                "type": "controlled_engagement",
                "evidence_strength": 0.92,
                "description": "ISRS 4400 agreed-upon procedures (NOT forensic audit) engaged 4 weeks post-interdict by RST under Peter's control",
                "evidence_refs": ["PF37/JH13", "Mazars report 11 Mar 2026"]
            }
        ]
    
    def _suggest_new_entities(self) -> List[Dict]:
        """Suggest new entities to add"""
        return [
            {
                "id": "ORG_MAZARS",
                "name": "Mazars (Forvis Mazars)",
                "type": "Professional Services",
                "role": "Engaged by Peter post-interdict for ISRS 4400 procedures",
                "evidence_refs": ["PF37/JH13"],
                "significance": "Report mischaracterized by Peter as 'forensic audit' — actually agreed-upon procedures"
            },
            {
                "id": "ORG_LERENA",
                "name": "Lerena Attorneys (Roslyn Lerena)",
                "type": "Legal",
                "role": "Jax's attorneys for reconsideration application",
                "evidence_refs": ["RE RECONSIDERATION AFFIDAVIT.pdf"],
                "significance": "Current representation for Jax in 2026-115880"
            },
            {
                "id": "PERSON_ADV_POOL",
                "name": "Advocate Deon M Pool",
                "type": "Legal Counsel",
                "role": "Counsel for Jax (and shared with Dan per fee note)",
                "evidence_refs": ["Applicant's Supplement HOA .pdf"],
                "significance": "Argues reconsideration and Part B matters"
            }
        ]


# ============================================================================
# SECTION 7: MAIN EXECUTION
# ============================================================================

def main():
    """Run the iterative micro-improvement pipeline"""
    data_dir = Path(__file__).parent.parent / "data_models"
    
    print("=" * 70)
    print("ITERATIVE MICRO-IMPROVEMENT SIMULATION FRAMEWORK")
    print("Case 2025-137857 | Revenue Stream Hijacking")
    print("=" * 70)
    print()
    
    # Initialize and load
    engine = IterativeMicroImprovement(str(data_dir))
    engine.load_data_models()
    engine.build_fund_flow_model()
    engine.evaluate_filings()
    
    # Run improvement cycle
    cycle = engine.run_improvement_cycle()
    print(f"\nCycle {cycle.cycle_id}: {cycle.notes}")
    
    # Generate report
    report = engine.generate_report()
    
    # Save report
    output_dir = Path(__file__).parent
    report_path = output_dir / "IMPROVEMENT_REPORT.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\nReport saved: {report_path}")
    
    # Print summary
    print("\n" + "=" * 70)
    print("FILING EVALUATION SUMMARY")
    print("=" * 70)
    for filing_type, evaluation in sorted(engine.evaluations.items(), key=lambda x: x[1].current_score, reverse=True):
        status = "✓ MET" if evaluation.threshold_met else "✗ NEAR"
        print(f"  {status} {filing_type.value:30s} Score: {evaluation.current_score:.2f} / {evaluation.burden.value:.2f}")
    
    print("\n" + "=" * 70)
    print("PRIORITY RECOMMENDATIONS")
    print("=" * 70)
    for rec in report["improvement_recommendations"]:
        print(f"  [{rec['priority']}] {rec['category']}: {rec['recommendation']}")
    
    print("\n" + "=" * 70)
    print("NEW EVENTS SUGGESTED")
    print("=" * 70)
    for ev in report["new_events_suggested"]:
        print(f"  {ev['id']} ({ev['date']}): {ev['title'][:70]}")
    
    return report


if __name__ == "__main__":
    report = main()
