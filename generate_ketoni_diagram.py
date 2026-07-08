import os

diagram = """%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3182ce', 'primaryTextColor': '#fff', 'lineColor': '#718096'}}}%%
flowchart TB
    subgraph KETONI_STRUCTURE["Ketoni Investment Structure & Conflict of Interest"]
        direction TB
        
        RYNETTE["👤 Rynette Farrar<br/>━━━━━━━━━━━━━━━━<br/>Appointed Bantjies as Trustee"]
        
        FFT["🏛️ Faucitt Family Trust (FFT)<br/>━━━━━━━━━━━━━━━━<br/>Trustees: Peter Faucitt, Danie Bantjies<br/>Beneficiaries: Jacqueline & Daniel"]
        
        KETONI["🏢 Ketoni Investment Holdings<br/>━━━━━━━━━━━━━━━━<br/>Reg: 2023/562189/07<br/>Director: Kevin Derrick"]
        
        GEORGE_GROUP["🏢 The George Group<br/>━━━━━━━━━━━━━━━━<br/>Reg: 2018/618716/07<br/>CEO: Kevin Derrick<br/>CFO: Danie Bantjies"]
        
        DERRICK_TRUST["🏛️ Kevin Derrick Trust<br/>━━━━━━━━━━━━━━━━<br/>Trustee: Kevin Derrick"]
    end

    %% Ownership & Investment Flows
    FFT ==>|"Invests R9.8M<br/>Holds 100% A-Ordinary Shares<br/>Gets 90% Distributions"| KETONI
    DERRICK_TRUST -->|"Invests R1,000<br/>Holds 100% Ordinary Shares<br/>Gets 10% Distributions"| KETONI
    KETONI ==>|"Invests R9.8M<br/>Holds 8.14% Shares (456 shares)"| GEORGE_GROUP
    
    %% Control & Conflict Relationships
    RYNETTE -.->|"Appoints (July 2024)"| FFT
    GEORGE_GROUP -.->|"Generates Returns for"| KETONI
    
    %% The Conflict
    BANTJIES_CFO(("Danie Bantjies<br/>(CFO Role)")) -.- GEORGE_GROUP
    BANTJIES_TRUSTEE(("Danie Bantjies<br/>(Trustee Role)")) -.- FFT
    BANTJIES_CFO <==>|"MASSIVE CONFLICT OF INTEREST<br/>Fiduciary Duty vs Professional Loyalty"| BANTJIES_TRUSTEE

    %% Styling
    classDef trust fill:#805ad5,stroke:#6b46c1,color:#fff,stroke-width:2px
    classDef company fill:#3182ce,stroke:#2c5282,color:#fff,stroke-width:2px
    classDef person fill:#dd6b20,stroke:#c05621,color:#fff,stroke-width:2px
    classDef conflict fill:#e53e3e,stroke:#c53030,color:#fff,stroke-width:3px
    
    class FFT,DERRICK_TRUST trust
    class KETONI,GEORGE_GROUP company
    class RYNETTE person
    class BANTJIES_CFO,BANTJIES_TRUSTEE conflict
"""

with open('/home/ubuntu/projects/case-92eda837/ketoni_conflict_structure.mmd', 'w') as f:
    f.write(diagram)
    
print("Generated ketoni_conflict_structure.mmd")
