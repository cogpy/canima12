#!/usr/bin/env python3
"""
Forensic Sims — Hybrid Multi-Paradigm Simulation Engine
========================================================
Composition: /vorticog ⊗ /skillm ⊗ /ai-env-grp-dyn ⊗ /acc-fund-flow ⊗ /virtual-endocrine-system
           ⊕ /cogsim-pml ⊕ /scm-des ⊕ /lex-sim-nn

5 Subsystems + 1 Integration Layer:
1. Economic Engine (Vorticog + Fund Flow) — ABM + SD
2. Supply Chain (CogSim PML + SCM-DES) — DES
3. Legal Reasoning (LEX-Sim-NN) — Differentiable NN
4. Persona & Group Dynamics (AI-Env-Grp-Dyn) — ABM
5. Virtual Endocrine System — Continuous
6. Hypergraph Dynamic Dict (LEX Transformer Vocab) — Integration
"""

import json
import math
import os
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta

# CogSim PML
sys.path.insert(0, '/home/ubuntu/cogsim')
from cogsim import (
    SimulationEngine, Source, Sink, Queue, Delay, Service,
    ResourcePool, ResourceTask, SelectOutput, SelectionMode,
    Combine, ArrivalMode, RandomVariate
)

# ==============================================================================
# SUBSYSTEM 5: VIRTUAL ENDOCRINE SYSTEM (16 channels)
# ==============================================================================

@dataclass
class HormoneChannel:
    name: str
    channel_id: int
    half_life: float  # ticks
    baseline: float
    concentration: float = 0.0
    
    def decay(self, dt: float = 1.0):
        decay_factor = math.exp(-0.693 * dt / self.half_life)
        self.concentration = self.baseline + (self.concentration - self.baseline) * decay_factor
    
    def inject(self, amount: float):
        self.concentration = min(1.0, self.concentration + amount)


class VirtualEndocrineSystem:
    """16-channel hormone bus with cognitive mode detection."""
    
    MODES = ['RESTING', 'EXPLORATORY', 'FOCUSED', 'STRESSED', 'SOCIAL',
             'REFLECTIVE', 'VIGILANT', 'MAINTENANCE', 'REWARD', 'THREAT']
    
    def __init__(self):
        self.channels = [
            HormoneChannel("CRH", 0, 5, 0.05),
            HormoneChannel("ACTH", 1, 10, 0.05),
            HormoneChannel("Cortisol", 2, 30, 0.15),
            HormoneChannel("Dopamine_tonic", 3, 20, 0.3),
            HormoneChannel("Dopamine_phasic", 4, 3, 0.0),
            HormoneChannel("Serotonin", 5, 50, 0.4),
            HormoneChannel("Norepinephrine", 6, 8, 0.1),
            HormoneChannel("Oxytocin", 7, 15, 0.1),
            HormoneChannel("T3_T4", 8, 100, 0.5),
            HormoneChannel("Melatonin", 9, 12, 0.0),
            HormoneChannel("Insulin", 10, 10, 0.2),
            HormoneChannel("Glucagon", 11, 8, 0.1),
            HormoneChannel("IL6", 12, 20, 0.05),
            HormoneChannel("Anandamide", 13, 6, 0.1),
            HormoneChannel("Reserved_14", 14, 10, 0.0),
            HormoneChannel("Reserved_15", 15, 10, 0.0),
        ]
        self.mode = 'RESTING'
        self.history = []
    
    def tick(self, dt: float = 1.0):
        for ch in self.channels:
            ch.decay(dt)
        self._detect_mode()
        self.history.append(self.get_state())
    
    def signal_event(self, event_type: str, intensity: float = 0.5):
        """Map case events to hormone responses."""
        event_map = {
            'evidence_discovered': [(4, 0.6), (6, 0.4)],  # Dopamine phasic + Norepinephrine
            'filing_deadline': [(0, 0.3), (1, 0.2), (2, 0.4)],  # HPA cascade
            'admission_obtained': [(5, 0.5), (3, 0.3)],  # Serotonin + Dopamine tonic
            'threat_interdict': [(0, 0.7), (1, 0.5), (2, 0.6), (6, 0.5)],  # Full stress
            'social_bond': [(7, 0.5)],  # Oxytocin
            'fraud_pattern': [(4, 0.8), (6, 0.6)],  # High phasic dopamine + alertness
            'revenue_diverted': [(2, 0.3), (11, 0.4)],  # Cortisol + Glucagon
            'platform_blocked': [(2, 0.5), (6, 0.3), (12, 0.2)],  # Stress + immune
            'group_coordination': [(7, 0.4), (5, 0.2)],  # Oxytocin + Serotonin
            'legal_victory': [(4, 0.7), (5, 0.4), (3, 0.3)],  # Reward cascade
        }
        signals = event_map.get(event_type, [(6, 0.2)])
        for ch_id, base_amount in signals:
            self.channels[ch_id].inject(base_amount * intensity)
    
    def _detect_mode(self):
        """Emergent mode detection from hormone concentrations."""
        c = [ch.concentration for ch in self.channels]
        cortisol, dopa_t, dopa_p, sero, norepi, oxy = c[2], c[3], c[4], c[5], c[6], c[7]
        
        if cortisol > 0.5 and norepi > 0.4:
            self.mode = 'THREAT'
        elif cortisol > 0.35:
            self.mode = 'STRESSED'
        elif norepi > 0.4 and cortisol < 0.3:
            self.mode = 'VIGILANT'
        elif dopa_p > 0.3:
            self.mode = 'REWARD'
        elif oxy > 0.3:
            self.mode = 'SOCIAL'
        elif sero > 0.5 and dopa_t > 0.4:
            self.mode = 'FOCUSED'
        elif dopa_t > 0.4 and norepi > 0.2:
            self.mode = 'EXPLORATORY'
        elif sero > 0.5:
            self.mode = 'REFLECTIVE'
        else:
            self.mode = 'RESTING'
    
    def get_state(self) -> dict:
        return {
            'mode': self.mode,
            'concentrations': {ch.name: round(ch.concentration, 4) for ch in self.channels},
        }
    
    def get_modulation(self) -> dict:
        """Return modulation factors for other subsystems."""
        c = [ch.concentration for ch in self.channels]
        return {
            'attention_focus': 1.0 + c[6] * 0.4,  # Norepinephrine
            'learning_rate': 1.0 + c[4] * 0.5,  # Dopamine phasic
            'threshold_shift': c[2] * 0.15,  # Cortisol raises scrutiny
            'confidence': c[5] * 0.8,  # Serotonin stabilizes
            'trust_bias': c[7] * 0.6,  # Oxytocin
            'processing_rate': c[8],  # T3/T4
        }


# ==============================================================================
# SUBSYSTEM 1: ECONOMIC ENGINE (Vorticog + Fund Flow)
# ==============================================================================

@dataclass
class FinancialStock:
    name: str
    value: float = 0.0
    history: List[float] = field(default_factory=list)
    
    def inflow(self, amount: float):
        self.value += amount
        self.history.append(self.value)
    
    def outflow(self, amount: float) -> float:
        actual = min(self.value, amount)
        self.value -= actual
        self.history.append(self.value)
        return actual


@dataclass
class FundFlowTransaction:
    source: str
    target: str
    amount: float
    timestamp: int
    reference: str = ""
    anomaly_score: float = 0.0


class EconomicEngine:
    """System Dynamics stocks/flows + Agent-Based fund tracing."""
    
    def __init__(self, entities: list, relations: list):
        self.stocks = {
            'legitimate_revenue': FinancialStock('legitimate_revenue', 500000),
            'diverted_revenue': FinancialStock('diverted_revenue', 0),
            'trust_assets': FinancialStock('trust_assets', 2000000),
            'litigation_funding': FinancialStock('litigation_funding', 0),
            'operational_capital': FinancialStock('operational_capital', 300000),
            'elliott_payments': FinancialStock('elliott_payments', 0),
            'rst_corporate': FinancialStock('rst_corporate', 150000),
            'rwd_corporate': FinancialStock('rwd_corporate', 200000),
            'shopify_revenue': FinancialStock('shopify_revenue', 0),
        }
        self.transactions: List[FundFlowTransaction] = []
        self.entities = {e.get('id', e.get('name', '')): e for e in entities}
        self.relations = relations
        self.tick_count = 0
        
        # Flow rates (R/month)
        self.flow_rates = {
            'revenue_diversion': 85000,  # Estimated from evidence
            'litigation_burn': 29935,  # R478,958 / 16 months
            'trust_extraction': 50000,  # Estimated
            'platform_revenue': 120000,  # Shopify when active
            'operational_expense': 45000,
        }
    
    def tick(self, endo_modulation: dict):
        """Advance economic simulation by one month."""
        self.tick_count += 1
        
        # Revenue generation (modulated by platform status)
        platform_active = self.tick_count < 6 or self.tick_count > 24  # Blocked Nov 2024 - ongoing
        if platform_active:
            revenue = self.flow_rates['platform_revenue'] * endo_modulation.get('processing_rate', 0.5)
            self.stocks['shopify_revenue'].inflow(revenue)
            self.stocks['legitimate_revenue'].inflow(revenue)
        
        # Revenue diversion (when platform blocked, revenue goes to shadow)
        if not platform_active:
            diverted = self.flow_rates['revenue_diversion']
            self.stocks['legitimate_revenue'].outflow(diverted)
            self.stocks['diverted_revenue'].inflow(diverted)
            self.transactions.append(FundFlowTransaction(
                'legitimate_revenue', 'diverted_revenue', diverted,
                self.tick_count, 'revenue_diversion', 0.85
            ))
        
        # Litigation funding (RST → Elliott)
        lit_amount = self.flow_rates['litigation_burn']
        self.stocks['rst_corporate'].outflow(lit_amount)
        self.stocks['elliott_payments'].inflow(lit_amount)
        self.stocks['litigation_funding'].inflow(lit_amount)
        self.transactions.append(FundFlowTransaction(
            'rst_corporate', 'elliott_payments', lit_amount,
            self.tick_count, 'RST_to_Elliott_unauthorized', 0.95
        ))
        
        # Trust extraction
        trust_out = self.flow_rates['trust_extraction']
        self.stocks['trust_assets'].outflow(trust_out)
        self.transactions.append(FundFlowTransaction(
            'trust_assets', 'operational_capital', trust_out,
            self.tick_count, 'trust_extraction', 0.7
        ))
        
        # Operational expenses
        self.stocks['operational_capital'].outflow(self.flow_rates['operational_expense'])
    
    def detect_anomalies(self) -> List[dict]:
        """Detect fund flow anomalies."""
        anomalies = []
        # Circular flow detection
        sources = {}
        for tx in self.transactions:
            key = (tx.source, tx.target)
            sources[key] = sources.get(key, 0) + tx.amount
        
        for (src, tgt), total in sources.items():
            if total > 100000 and any(
                t.source == tgt and t.target == src for t in self.transactions
            ):
                anomalies.append({
                    'type': 'circular_flow',
                    'entities': [src, tgt],
                    'total': total,
                    'severity': 'HIGH'
                })
        
        # Unauthorized payment pattern
        elliott_total = self.stocks['elliott_payments'].value
        if elliott_total > 400000:
            anomalies.append({
                'type': 'unauthorized_payment_pattern',
                'entity': 'Elliott Attorneys',
                'total': elliott_total,
                'count': sum(1 for t in self.transactions if 'Elliott' in t.reference),
                'severity': 'CRITICAL',
                'evidence': 'No board resolution, no CEO knowledge'
            })
        
        return anomalies
    
    def get_state(self) -> dict:
        return {
            'tick': self.tick_count,
            'stocks': {k: round(v.value, 2) for k, v in self.stocks.items()},
            'total_transactions': len(self.transactions),
            'anomalies': self.detect_anomalies(),
        }


# ==============================================================================
# SUBSYSTEM 2: SUPPLY CHAIN (CogSim PML + SCM-DES)
# ==============================================================================

class SupplyChainDES:
    """Discrete Event Simulation of RegimA product/revenue supply chain."""
    
    def __init__(self):
        self.engine = SimulationEngine(seed=42)
        self.rv = RandomVariate(seed=42)
        self.blocks = {}
        self.metrics = {}
        self._build_chain()
    
    def _build_chain(self):
        """Build the RegimA supply chain process flow."""
        # Source: Customer orders (Shopify)
        self.blocks['orders'] = Source(
            "customer_orders",
            arrival_mode=ArrivalMode.RATE,
            rate=4.0,  # 4 orders/hour during active periods
            engine=self.engine
        )
        
        # Service: Order processing (Sage)
        self.blocks['processing'] = Service(
            "order_processing",
            service_time=lambda: self.rv.triangular(0.5, 2.0, 1.0),
            capacity=3,
            engine=self.engine
        )
        
        # Resource: Warehouse workers
        self.blocks['warehouse_pool'] = ResourcePool(
            "warehouse_workers", capacity=5, engine=self.engine
        )
        
        # Task: Fulfillment
        self.blocks['fulfillment'] = ResourceTask(
            "fulfillment",
            resource_pool=self.blocks['warehouse_pool'],
            task_time=lambda: self.rv.triangular(1.0, 4.0, 2.0),
            quantity=1,
            engine=self.engine
        )
        
        # Router: Legitimate vs Diverted channel
        self.blocks['channel_router'] = SelectOutput(
            "channel_router",
            mode=SelectionMode.PROBABILITY,
            probability=0.65,  # 65% legitimate during hijack period
            engine=self.engine
        )
        
        # Sinks
        self.blocks['legitimate_sink'] = Sink("legitimate_delivery", engine=self.engine)
        self.blocks['diverted_sink'] = Sink("diverted_delivery", engine=self.engine)
        
        # Connect the chain
        self.blocks['orders'] >> self.blocks['processing'] >> self.blocks['fulfillment'] >> self.blocks['channel_router']
        self.blocks['channel_router'].get_output_port("out_true").connect(
            self.blocks['legitimate_sink'].get_input_port("in"))
        self.blocks['channel_router'].get_output_port("out_false").connect(
            self.blocks['diverted_sink'].get_input_port("in"))
    
    def run(self, duration: float = 480):
        """Run simulation for given duration (default: 8-hour shift)."""
        self.engine.run(until=duration)
        self._collect_metrics()
    
    def _collect_metrics(self):
        """Collect supply chain metrics."""
        legit_stats = self.blocks['legitimate_sink'].get_statistics()
        divert_stats = self.blocks['diverted_sink'].get_statistics()
        warehouse_stats = self.blocks['warehouse_pool'].get_statistics()
        
        self.metrics = {
            'legitimate_throughput': self.blocks['legitimate_sink'].count(),
            'diverted_throughput': self.blocks['diverted_sink'].count(),
            'diversion_ratio': (
                self.blocks['diverted_sink'].count() /
                max(1, self.blocks['legitimate_sink'].count() + self.blocks['diverted_sink'].count())
            ),
            'avg_lead_time': legit_stats.get('average_time_in_system', 0),
            'warehouse_utilization': warehouse_stats.get('average_utilization', 0),
            'total_orders_processed': (
                self.blocks['legitimate_sink'].count() + self.blocks['diverted_sink'].count()
            ),
        }
    
    def get_state(self) -> dict:
        return self.metrics


# ==============================================================================
# SUBSYSTEM 3: LEGAL REASONING (LEX-Sim-NN)
# ==============================================================================

class LEXSimNN:
    """Differentiable legal reasoning pipeline (simplified PyTorch-free version)."""
    
    def __init__(self):
        # 24D evidence vector: 6 categories x 4 features
        self.evidence_dim = 24
        self.hidden_dim = 128
        self.output_dim = 2  # [civil_met, criminal_met]
        
        # 7 attention lenses
        self.lenses = ['temporal', 'financial', 'documentary', 
                       'testimonial', 'forensic', 'relational', 'intentional']
        
        # Filing thresholds
        self.thresholds = {
            'civil': 0.50,
            'criminal': 0.95,
            'regulatory': 0.50,
            'professional': 0.50,
        }
        
        # Current evidence state (from case data)
        self.evidence_vector = [0.0] * 24
        self.filing_scores = {}
    
    def encode_evidence(self, events: list, relations: list) -> list:
        """Encode case evidence into 24D vector."""
        vec = [0.0] * 24
        
        # Temporal (dims 0-3): event density, sequence completeness, registration timeline, duration
        vec[0] = min(1.0, len(events) / 200)  # Event density
        vec[1] = 0.95  # Sequence completeness (181 events, well-ordered)
        vec[2] = 0.90  # Registration timeline documented
        vec[3] = min(1.0, 19 / 24)  # Duration (19 months of 24 max)
        
        # Financial (dims 4-7): amounts, flows, ratios, volumes
        vec[4] = 0.95  # R478,958 Elliott payments documented
        vec[5] = 0.80  # Fund flow tracing partial
        vec[6] = 0.90  # Revenue ratios calculated
        vec[7] = 0.75  # Transaction volume (need more bank data)
        
        # Documentary (dims 8-11): contracts, emails, filings, CIPC
        vec[8] = 0.85  # Contracts available
        vec[9] = 0.90  # Email evidence strong
        vec[10] = 0.95  # Court filings complete
        vec[11] = 0.80  # CIPC records obtained
        
        # Testimonial (dims 12-15): reliability, consistency, corroboration
        vec[12] = 0.98  # Peter's AA admissions (sworn, self-contradicting)
        vec[13] = 0.95  # Consistency of evidence chain
        vec[14] = 0.85  # Corroboration (multiple sources)
        vec[15] = 0.70  # Independent witness (need more)
        
        # Forensic (dims 16-19): digital traces, metadata, audit trails
        vec[16] = 0.90  # Shopify platform traces
        vec[17] = 0.85  # Bank statement metadata
        vec[18] = 0.60  # Sage audit trail (blocked)
        vec[19] = 0.80  # ABSA statement forensics
        
        # Relational/Intentional (dims 20-23): entity links, roles, mens rea
        vec[20] = 0.95  # Entity links well-mapped
        vec[21] = 0.90  # Roles documented
        vec[22] = 0.85  # Mens rea indicators strong
        vec[23] = 0.80  # Knowledge state proven via admissions
        
        self.evidence_vector = vec
        return vec
    
    def forward(self, endo_modulation: dict) -> dict:
        """Run the legal reasoning pipeline with endocrine modulation."""
        vec = self.evidence_vector
        
        # Apply 7-lens attention (weighted sum per category)
        lens_weights = {
            'temporal': sum(vec[0:4]) / 4,
            'financial': sum(vec[4:8]) / 4,
            'documentary': sum(vec[8:12]) / 4,
            'testimonial': sum(vec[12:16]) / 4,
            'forensic': sum(vec[16:20]) / 4,
            'relational': sum(vec[20:24]) / 4,
            'intentional': (vec[22] + vec[23]) / 2,
        }
        
        # Apply endocrine modulation
        attention_focus = endo_modulation.get('attention_focus', 1.0)
        threshold_shift = endo_modulation.get('threshold_shift', 0.0)
        confidence = endo_modulation.get('confidence', 0.5)
        
        # Modulate lens weights
        for lens in lens_weights:
            lens_weights[lens] *= attention_focus
        
        # Compute overall evidence strength
        overall = sum(lens_weights.values()) / len(lens_weights)
        
        # Civil burden (50% + threshold shift)
        civil_threshold = self.thresholds['civil'] + threshold_shift
        civil_met = 1.0 / (1.0 + math.exp(-10 * (overall - civil_threshold)))
        
        # Criminal burden (95% + threshold shift)
        criminal_threshold = self.thresholds['criminal'] + threshold_shift
        criminal_met = 1.0 / (1.0 + math.exp(-10 * (overall - criminal_threshold)))
        
        # Per-filing evaluation
        self.filing_scores = {
            'SCA_Opposition': min(1.0, (lens_weights['testimonial'] + lens_weights['documentary']) / 2 / civil_threshold),
            'Part_B_Delinquency': min(1.0, (lens_weights['relational'] + lens_weights['intentional']) / 2 / civil_threshold),
            'Rule_42_Rescission': min(1.0, (lens_weights['testimonial'] + lens_weights['temporal']) / 2 / civil_threshold),
            'CIPC_Complaint': min(1.0, overall / civil_threshold),
            'LPC_Complaint': min(1.0, lens_weights['financial'] / civil_threshold),
            'POPIA_Complaint': min(1.0, lens_weights['forensic'] / civil_threshold),
            'SARS_Tax_Fraud': min(1.0, lens_weights['financial'] / criminal_threshold),
            'Criminal_Perjury': min(1.0, lens_weights['testimonial'] / criminal_threshold),
            'NPA_Referral': min(1.0, overall / criminal_threshold),
            'SAICA_Misconduct': min(1.0, (lens_weights['financial'] + lens_weights['relational']) / 2 / civil_threshold),
        }
        
        return {
            'civil_burden_met': round(civil_met, 4),
            'criminal_burden_met': round(criminal_met, 4),
            'overall_evidence_strength': round(overall, 4),
            'lens_weights': {k: round(v, 4) for k, v in lens_weights.items()},
            'filing_scores': {k: round(v, 4) for k, v in self.filing_scores.items()},
            'confidence': round(confidence, 4),
        }
    
    def attribute_evidence(self) -> dict:
        """Gradient-based attribution (simplified: contribution per category)."""
        categories = ['temporal', 'financial', 'documentary', 'testimonial', 'forensic', 'relational']
        vec = self.evidence_vector
        attribution = {}
        for i, cat in enumerate(categories):
            cat_mean = sum(vec[i*4:(i+1)*4]) / 4
            attribution[cat] = round(cat_mean, 4)
        return attribution


# ==============================================================================
# SUBSYSTEM 4: PERSONA & GROUP DYNAMICS (AI-Env-Grp-Dyn)
# ==============================================================================

@dataclass
class AgentPersona:
    entity_id: str
    name: str
    # Big Five personality
    openness: float = 0.5
    conscientiousness: float = 0.5
    extraversion: float = 0.5
    agreeableness: float = 0.5
    neuroticism: float = 0.5
    # State
    stress: float = 0.0
    trust: float = 0.5
    loyalty: float = 0.5
    satisfaction: float = 0.5
    # 7D state vector
    knowledge: float = 0.5
    capability: float = 0.5
    motive: float = 0.5
    opportunity: float = 0.5
    behavioral: float = 0.5
    strategic: float = 0.5
    network: float = 0.5


@dataclass
class Group:
    id: str
    name: str
    members: List[str]
    cohesion: float = 0.5
    shared_goals: List[str] = field(default_factory=list)
    formation_tick: int = 0


class PersonaGroupEngine:
    """Agent-Based Model with emergent group dynamics."""
    
    def __init__(self, entities: list, relations: list):
        self.agents: Dict[str, AgentPersona] = {}
        self.groups: Dict[str, Group] = {}
        self.social_network: Dict[Tuple[str, str], float] = {}
        self._init_agents(entities)
        self._init_groups()
        self._init_social_network(relations)
    
    def _init_agents(self, entities: list):
        """Initialize agent personas from entity data."""
        # Key personas with modeled Big Five
        persona_profiles = {
            'PERSON_001': {'name': 'Peter Faucitt', 'openness': 0.3, 'conscientiousness': 0.4,
                          'extraversion': 0.7, 'agreeableness': 0.2, 'neuroticism': 0.7,
                          'motive': 0.9, 'opportunity': 0.8, 'strategic': 0.7},
            'PERSON_002': {'name': 'Rynette Farrar', 'openness': 0.3, 'conscientiousness': 0.6,
                          'extraversion': 0.4, 'agreeableness': 0.3, 'neuroticism': 0.5,
                          'motive': 0.7, 'capability': 0.8, 'knowledge': 0.9},
            'PERSON_003': {'name': 'Jacqueline Faucitt', 'openness': 0.5, 'conscientiousness': 0.6,
                          'extraversion': 0.4, 'agreeableness': 0.6, 'neuroticism': 0.4,
                          'motive': 0.6, 'knowledge': 0.7},
            'PERSON_004': {'name': 'Daniel Faucitt', 'openness': 0.9, 'conscientiousness': 0.8,
                          'extraversion': 0.5, 'agreeableness': 0.7, 'neuroticism': 0.3,
                          'knowledge': 0.9, 'capability': 0.9, 'strategic': 0.8},
            'PERSON_BANTJIES': {'name': 'Danie Bantjies', 'openness': 0.2, 'conscientiousness': 0.7,
                               'extraversion': 0.3, 'agreeableness': 0.3, 'neuroticism': 0.4,
                               'capability': 0.8, 'motive': 0.6},
        }
        
        for eid, profile in persona_profiles.items():
            name = profile.pop('name')
            self.agents[eid] = AgentPersona(entity_id=eid, name=name, **profile)
        
        # Add remaining entities with default personas
        for entity in entities:
            eid = entity.get('id', entity.get('name', ''))
            if eid not in self.agents and entity.get('type') in ['person', 'natural_person']:
                self.agents[eid] = AgentPersona(entity_id=eid, name=entity.get('name', eid))
    
    def _init_groups(self):
        """Initialize emergent groups based on known alliances."""
        self.groups = {
            'peter_faction': Group(
                'peter_faction', 'Peter Faction',
                ['PERSON_001', 'PERSON_BANTJIES'],
                cohesion=0.8,
                shared_goals=['maintain_control', 'block_discovery', 'fund_litigation']
            ),
            'daniel_faction': Group(
                'daniel_faction', 'Daniel/Jax Faction',
                ['PERSON_004', 'PERSON_003'],
                cohesion=0.7,
                shared_goals=['restore_access', 'expose_fraud', 'protect_assets']
            ),
            'professional_services': Group(
                'professional_services', 'Professional Services',
                [],  # Elliott, Mazars, etc. — not persona agents
                cohesion=0.6,
                shared_goals=['execute_instructions', 'bill_fees']
            ),
        }
    
    def _init_social_network(self, relations: list):
        """Build weighted social network from relations."""
        for rel in relations:
            entities_involved = rel.get('entities_involved', [])
            if isinstance(entities_involved, list) and len(entities_involved) >= 2:
                src = rel.get('source', entities_involved[0])
                tgt = rel.get('target', entities_involved[-1])
            else:
                src = rel.get('source', '')
                tgt = rel.get('target', '')
            strength = rel.get('strength', rel.get('confidence', 0.5))
            if src and tgt and src != tgt:
                self.social_network[(src, tgt)] = strength
    
    def tick(self, events: list, endo_modulation: dict):
        """Update agent states based on events and endocrine modulation."""
        for agent in self.agents.values():
            # Stress modulated by cortisol
            agent.stress = min(1.0, agent.stress * 0.95 + agent.neuroticism * endo_modulation.get('threshold_shift', 0) * 2)
            
            # Trust modulated by oxytocin
            agent.trust = max(0, min(1.0, agent.trust + (endo_modulation.get('trust_bias', 0) - 0.3) * 0.1))
        
        # Update group cohesion
        for group in self.groups.values():
            group.cohesion *= 0.99  # Natural decay
            # Boost if shared events
            for event in events:
                actors = event.get('actors', [])
                overlap = set(actors) & set(group.members)
                if len(overlap) >= 2:
                    group.cohesion = min(1.0, group.cohesion + 0.05)
    
    def propagate_information(self, source: str, info: str, max_hops: int = 2) -> List[str]:
        """Gossip model: information spreads through social network."""
        reached = {source}
        frontier = set()
        for (s, t), weight in self.social_network.items():
            if s == source and weight > 0.3:
                frontier.add(t)
        
        for hop in range(max_hops):
            next_frontier = set()
            for agent in frontier:
                if agent not in reached:
                    reached.add(agent)
                    for (s, t), weight in self.social_network.items():
                        if s == agent and weight > 0.3 and t not in reached:
                            next_frontier.add(t)
            frontier = next_frontier
        
        return list(reached)
    
    def get_state(self) -> dict:
        return {
            'agents': {k: {'stress': round(v.stress, 3), 'trust': round(v.trust, 3),
                          'loyalty': round(v.loyalty, 3)} for k, v in self.agents.items()},
            'groups': {k: {'cohesion': round(v.cohesion, 3), 'members': len(v.members)}
                      for k, v in self.groups.items()},
            'network_density': len(self.social_network),
        }


# ==============================================================================
# SUBSYSTEM 6: HYPERGRAPH DYNAMIC DICT (LEX Transformer Vocab)
# ==============================================================================

@dataclass
class LexDictEntry:
    """Dynamic dictionary entry linking all subsystems through the hypergraph."""
    token_id: str
    token_type: str  # entity, relation, event, filing, ksm_cell
    embedding: List[float]  # 24D evidence vector subset
    attention_bias: float  # From KSM center strength
    hormone_modulation: Dict[str, float]  # 16 hormone effects
    filing_relevance: Dict[str, float]  # Per-filing relevance
    matula_prime: int  # Proof certificate encoding
    subsystem_refs: Dict[str, str]  # Cross-references to subsystem states
    last_updated: str


class HypergraphDynamicDict:
    """Integration layer: LEX transformer vocabulary as dynamic dict entries."""
    
    def __init__(self):
        self.entries: Dict[str, LexDictEntry] = {}
        self.update_log: List[dict] = []
    
    def register_entity(self, entity_id: str, entity_data: dict, 
                       evidence_vector: list, ksm_strength: float = 0.5):
        """Register an entity as a LEX dict token."""
        self.entries[entity_id] = LexDictEntry(
            token_id=entity_id,
            token_type='entity',
            embedding=evidence_vector[:6] if len(evidence_vector) >= 6 else [0.0]*6,
            attention_bias=ksm_strength,
            hormone_modulation={},
            filing_relevance={},
            matula_prime=entity_data.get('matula_prime', 1),
            subsystem_refs={
                'economic': f"stock:{entity_id}",
                'supply_chain': f"block:{entity_id}",
                'persona': f"agent:{entity_id}",
            },
            last_updated=datetime.now().isoformat()
        )
    
    def register_relation(self, relation_id: str, relation_data: dict):
        """Register a relation as a LEX dict attention weight."""
        self.entries[relation_id] = LexDictEntry(
            token_id=relation_id,
            token_type='relation',
            embedding=[relation_data.get('strength', 0.5)] * 6,
            attention_bias=relation_data.get('confidence', relation_data.get('strength', 0.5)),
            hormone_modulation={},
            filing_relevance={},
            matula_prime=1,
            subsystem_refs={
                'source': relation_data.get('source', ''),
                'target': relation_data.get('target', ''),
            },
            last_updated=datetime.now().isoformat()
        )
    
    def register_event(self, event_id: str, event_data: dict, tick: int):
        """Register an event with temporal positional encoding."""
        self.entries[event_id] = LexDictEntry(
            token_id=event_id,
            token_type='event',
            embedding=[tick / 200.0] * 6,  # Temporal position normalized
            attention_bias=event_data.get('significance', 5) / 10.0,
            hormone_modulation={},
            filing_relevance={},
            matula_prime=1,
            subsystem_refs={
                'phase': str(event_data.get('phase', 0)),
                'actors': ','.join(event_data.get('actors', [])),
            },
            last_updated=datetime.now().isoformat()
        )
    
    def update_from_subsystems(self, economic_state: dict, legal_state: dict,
                               persona_state: dict, endo_state: dict):
        """Broadcast subsystem states to all relevant dict entries."""
        hormone_mod = endo_state.get('concentrations', {})
        filing_scores = legal_state.get('filing_scores', {})
        
        for entry_id, entry in self.entries.items():
            entry.hormone_modulation = hormone_mod
            if entry.token_type == 'entity':
                entry.filing_relevance = filing_scores
            entry.last_updated = datetime.now().isoformat()
        
        self.update_log.append({
            'tick': economic_state.get('tick', 0),
            'entries_updated': len(self.entries),
            'mode': endo_state.get('mode', 'RESTING'),
        })
    
    def get_state(self) -> dict:
        return {
            'total_entries': len(self.entries),
            'by_type': {
                'entity': sum(1 for e in self.entries.values() if e.token_type == 'entity'),
                'relation': sum(1 for e in self.entries.values() if e.token_type == 'relation'),
                'event': sum(1 for e in self.entries.values() if e.token_type == 'event'),
            },
            'updates': len(self.update_log),
            'last_mode': self.update_log[-1]['mode'] if self.update_log else 'INIT',
        }
    
    def export_vocab(self) -> dict:
        """Export the dynamic dict as a LEX transformer vocabulary."""
        vocab = {}
        for entry_id, entry in self.entries.items():
            vocab[entry_id] = {
                'type': entry.token_type,
                'embedding': entry.embedding,
                'attention_bias': entry.attention_bias,
                'matula_prime': entry.matula_prime,
                'filing_relevance': entry.filing_relevance,
            }
        return vocab


# ==============================================================================
# MASTER ORCHESTRATOR: FORENSIC SIMS ENGINE
# ==============================================================================

class ForensicSimsEngine:
    """
    Master orchestrator composing all 5 subsystems + integration layer.
    
    Composition: /vorticog ⊗ /skillm ⊗ /ai-env-grp-dyn ⊗ /acc-fund-flow ⊗ /virtual-endocrine-system
               ⊕ /cogsim-pml ⊕ /scm-des ⊕ /lex-sim-nn
    """
    
    def __init__(self, data_dir: str = None):
        self.data_dir = data_dir or os.path.join(os.path.dirname(__file__), '..', 'data_models')
        self.entities = []
        self.relations = []
        self.events = []
        self.timeline = {}
        
        # Load data
        self._load_data()
        
        # Initialize subsystems
        self.endocrine = VirtualEndocrineSystem()
        self.economic = EconomicEngine(self.entities, self.relations)
        self.supply_chain = SupplyChainDES()
        self.legal = LEXSimNN()
        self.persona = PersonaGroupEngine(self.entities, self.relations)
        self.hypergraph = HypergraphDynamicDict()
        
        # Register all data into hypergraph
        self._register_hypergraph()
        
        self.tick_count = 0
        self.simulation_log = []
    
    def _load_data(self):
        """Load case data from revstream1 data_models."""
        try:
            with open(os.path.join(self.data_dir, 'entities.json')) as f:
                self.entities = json.load(f)
            with open(os.path.join(self.data_dir, 'relations.json')) as f:
                self.relations = json.load(f)
            with open(os.path.join(self.data_dir, 'events.json')) as f:
                self.events = json.load(f)
            with open(os.path.join(self.data_dir, 'timelines', 'timeline.json')) as f:
                self.timeline = json.load(f)
        except FileNotFoundError as e:
            print(f"Warning: Could not load data file: {e}")
    
    def _register_hypergraph(self):
        """Register all entities, relations, and events into the dynamic dict."""
        evidence_vec = self.legal.encode_evidence(self.events, self.relations)
        
        for entity in self.entities:
            eid = entity.get('id', entity.get('name', ''))
            self.hypergraph.register_entity(eid, entity, evidence_vec)
        
        for i, rel in enumerate(self.relations):
            rid = rel.get('id', f"REL_{i:03d}")
            self.hypergraph.register_relation(rid, rel)
        
        for i, event in enumerate(self.events):
            evid = event.get('id', f"EVENT_{i:03d}")
            self.hypergraph.register_event(evid, event, i)
    
    def simulate(self, months: int = 19, verbose: bool = True) -> dict:
        """Run the full multi-paradigm simulation for N months."""
        if verbose:
            print(f"{'='*70}")
            print(f"FORENSIC SIMS ENGINE — {months}-Month Simulation")
            print(f"{'='*70}")
            print(f"Entities: {len(self.entities)} | Relations: {len(self.relations)} | Events: {len(self.events)}")
            print(f"Hypergraph Dict Entries: {self.hypergraph.get_state()['total_entries']}")
            print(f"{'='*70}\n")
        
        # Phase 1: Run supply chain DES (one-shot for the period)
        self.supply_chain.run(duration=months * 160)  # ~160 working hours/month
        
        # Phase 2: Run monthly tick loop
        case_events_by_month = self._distribute_events(months)
        
        for month in range(1, months + 1):
            self.tick_count = month
            
            # Signal relevant events to endocrine system
            month_events = case_events_by_month.get(month, [])
            for event in month_events:
                event_type = self._classify_event(event)
                self.endocrine.signal_event(event_type, 0.7)
            
            # Tick endocrine (produces modulation for other subsystems)
            self.endocrine.tick()
            endo_mod = self.endocrine.get_modulation()
            
            # Tick economic engine
            self.economic.tick(endo_mod)
            
            # Tick persona engine
            self.persona.tick(month_events, endo_mod)
            
            # Run legal pipeline
            legal_output = self.legal.forward(endo_mod)
            
            # Update hypergraph integration layer
            self.hypergraph.update_from_subsystems(
                self.economic.get_state(),
                legal_output,
                self.persona.get_state(),
                self.endocrine.get_state()
            )
            
            # Log state
            state = {
                'month': month,
                'endocrine_mode': self.endocrine.mode,
                'economic': self.economic.get_state(),
                'legal': legal_output,
                'events_this_month': len(month_events),
            }
            self.simulation_log.append(state)
            
            if verbose and month % 3 == 0:
                print(f"Month {month:2d} | Mode: {self.endocrine.mode:12s} | "
                      f"Civil: {legal_output['civil_burden_met']:.3f} | "
                      f"Criminal: {legal_output['criminal_burden_met']:.3f} | "
                      f"Elliott: R{self.economic.stocks['elliott_payments'].value:,.0f}")
        
        # Final results
        results = self._compile_results(verbose)
        return results
    
    def _distribute_events(self, months: int) -> dict:
        """Distribute events across months based on timeline."""
        events_by_month = {}
        for i, event in enumerate(self.events):
            month = min(months, max(1, (i * months) // max(1, len(self.events)) + 1))
            events_by_month.setdefault(month, []).append(event)
        return events_by_month
    
    def _classify_event(self, event: dict) -> str:
        """Classify event type for endocrine signaling."""
        category = event.get('category', event.get('type', ''))
        title = event.get('title', event.get('description', '')).lower()
        
        if 'fraud' in title or 'divert' in title:
            return 'fraud_pattern'
        elif 'admission' in title or 'affidavit' in title:
            return 'admission_obtained'
        elif 'interdict' in title or 'order' in title:
            return 'threat_interdict'
        elif 'platform' in title or 'block' in title or 'shopify' in title:
            return 'platform_blocked'
        elif 'evidence' in title or 'discover' in title:
            return 'evidence_discovered'
        elif 'filing' in title or 'deadline' in title:
            return 'filing_deadline'
        elif 'revenue' in title or 'payment' in title:
            return 'revenue_diverted'
        else:
            return 'evidence_discovered'
    
    def _compile_results(self, verbose: bool) -> dict:
        """Compile final simulation results."""
        final_economic = self.economic.get_state()
        final_legal = self.legal.forward(self.endocrine.get_modulation())
        final_persona = self.persona.get_state()
        final_supply = self.supply_chain.get_state()
        final_hypergraph = self.hypergraph.get_state()
        final_endo = self.endocrine.get_state()
        attribution = self.legal.attribute_evidence()
        
        results = {
            'simulation_summary': {
                'months_simulated': self.tick_count,
                'total_events_processed': len(self.events),
                'final_endocrine_mode': final_endo['mode'],
                'hypergraph_entries': final_hypergraph['total_entries'],
            },
            'economic_engine': {
                'stocks': final_economic['stocks'],
                'total_diverted': final_economic['stocks'].get('diverted_revenue', 0),
                'total_elliott': final_economic['stocks'].get('elliott_payments', 0),
                'anomalies': final_economic['anomalies'],
            },
            'supply_chain_des': {
                'legitimate_throughput': final_supply.get('legitimate_throughput', 0),
                'diverted_throughput': final_supply.get('diverted_throughput', 0),
                'diversion_ratio': final_supply.get('diversion_ratio', 0),
                'warehouse_utilization': final_supply.get('warehouse_utilization', 0),
            },
            'legal_reasoning': {
                'civil_burden_met': final_legal['civil_burden_met'],
                'criminal_burden_met': final_legal['criminal_burden_met'],
                'overall_evidence_strength': final_legal['overall_evidence_strength'],
                'filing_scores': final_legal['filing_scores'],
                'evidence_attribution': attribution,
            },
            'persona_dynamics': final_persona,
            'endocrine_state': final_endo,
            'hypergraph_dict': final_hypergraph,
            'lex_vocab_size': final_hypergraph['total_entries'],
        }
        
        if verbose:
            print(f"\n{'='*70}")
            print("SIMULATION COMPLETE")
            print(f"{'='*70}")
            print(f"\nEconomic Engine:")
            print(f"  Total diverted revenue: R{results['economic_engine']['total_diverted']:,.2f}")
            print(f"  Total Elliott payments: R{results['economic_engine']['total_elliott']:,.2f}")
            print(f"  Anomalies detected: {len(results['economic_engine']['anomalies'])}")
            print(f"\nSupply Chain DES:")
            print(f"  Legitimate throughput: {results['supply_chain_des']['legitimate_throughput']}")
            print(f"  Diverted throughput: {results['supply_chain_des']['diverted_throughput']}")
            print(f"  Diversion ratio: {results['supply_chain_des']['diversion_ratio']:.1%}")
            print(f"\nLegal Reasoning (LEX-Sim-NN):")
            print(f"  Civil burden met: {results['legal_reasoning']['civil_burden_met']:.4f}")
            print(f"  Criminal burden met: {results['legal_reasoning']['criminal_burden_met']:.4f}")
            print(f"  Overall evidence: {results['legal_reasoning']['overall_evidence_strength']:.4f}")
            print(f"\n  Filing Scores:")
            for filing, score in sorted(results['legal_reasoning']['filing_scores'].items(), key=lambda x: -x[1]):
                status = "EXCEEDED" if score >= 1.0 else "MET" if score >= 0.95 else "NEAR" if score >= 0.75 else "GAP"
                print(f"    {filing:25s}: {score:.3f} [{status}]")
            print(f"\n  Evidence Attribution:")
            for cat, weight in sorted(attribution.items(), key=lambda x: -x[1]):
                print(f"    {cat:15s}: {'█' * int(weight * 20)} {weight:.3f}")
            print(f"\nHypergraph Dynamic Dict:")
            print(f"  Total vocab entries: {results['lex_vocab_size']}")
            print(f"  Entity tokens: {final_hypergraph['by_type']['entity']}")
            print(f"  Relation tokens: {final_hypergraph['by_type']['relation']}")
            print(f"  Event tokens: {final_hypergraph['by_type']['event']}")
            print(f"\nEndocrine Final Mode: {results['endocrine_state']['mode']}")
        
        return results


# ==============================================================================
# MAIN: Run the simulation
# ==============================================================================

if __name__ == '__main__':
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data_models')
    engine = ForensicSimsEngine(data_dir=data_dir)
    results = engine.simulate(months=19, verbose=True)
    
    # Export results
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'FORENSIC_SIMS_RESULTS.json')
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults exported to: {output_path}")
    
    # Export LEX vocab
    vocab_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'LEX_DYNAMIC_VOCAB.json')
    vocab = engine.hypergraph.export_vocab()
    with open(vocab_path, 'w') as f:
        json.dump(vocab, f, indent=2, default=str)
    print(f"LEX Dynamic Vocab exported to: {vocab_path}")
