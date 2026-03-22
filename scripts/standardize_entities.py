import os, re

entities_dir = 'docs/entities'
type_mapping = {
    'PERSON': 'Person',
    '| Person |': 'Person',
    'Organization': 'Organization',
    '| Private Company |': 'Organization',
    '| Juristic Person |': 'Organization',
    'Standard Bank Business Account': 'Bank Account',
    'Bank Account (Group)': 'Bank Account',
    'law_firm': 'Organization',
    '| Legal Practice |': 'Organization',
    '| Organization (Law Firm) |': 'Organization',
    'Logistics Platform': 'Platform'
}

for f in os.listdir(entities_dir):
    if f.endswith('.md') and not f.startswith(('index', 'README', 'perpetrators', 'victims', 'organizations', 'persons')):
        path = os.path.join(entities_dir, f)
        with open(path, 'r') as fh:
            content = fh.read()
        
        # Check if it has a Type field
        type_match = re.search(r'\*\*Type[:\s]*\*\*\s*(.+)', content)
        if type_match:
            old_type = type_match.group(1).strip()
            new_type = type_mapping.get(old_type, 'Unknown')
            if old_type != new_type:
                content = content.replace(f'**Type:** {old_type}', f'**Type:** {new_type}')
                content = content.replace(f'**Type:** {old_type}  ', f'**Type:** {new_type}  ')
        else:
            # Try to infer type from filename
            inferred_type = 'Unknown'
            if f.startswith('PERSON_'): inferred_type = 'Person'
            elif f.startswith('ORG_'): inferred_type = 'Organization'
            elif f.startswith('BANK_'): inferred_type = 'Bank Account'
            elif f.startswith('DOMAIN_'): inferred_type = 'Domain'
            elif f.startswith('PLATFORM_'): inferred_type = 'Platform'
            elif f.startswith('TRUST_'): inferred_type = 'Trust'
            
            # Insert Type field after Role or at the beginning
            if '**Role:**' in content:
                content = content.replace('**Role:**', f'**Type:** {inferred_type}  \n**Role:**')
            else:
                # Insert after the first heading
                content = re.sub(r'^(# .+?\n)', f'\\1**Type:** {inferred_type}  \n', content, count=1)
        
        with open(path, 'w') as fh:
            fh.write(content)

print("Entities standardized.")
