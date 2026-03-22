import os, re

events_dir = 'docs/events'

for f in os.listdir(events_dir):
    if f.endswith('.md') and (f.startswith('EVENT_') or f.startswith('EVT-')):
        path = os.path.join(events_dir, f)
        with open(path, 'r') as fh:
            content = fh.read()
        
        # Check for missing fields
        has_date = bool(re.search(r'\*\*Date', content))
        has_type = bool(re.search(r'\*\*Type', content))
        has_entities = bool(re.search(r'\*\*Entit', content))
        has_source = bool(re.search(r'\*\*Source', content))
        
        if not (has_date and has_type and has_entities and has_source):
            # Find the metadata section or create one
            meta_match = re.search(r'## Event Metadata\n(.*?)\n##', content, re.DOTALL)
            if meta_match:
                meta_text = meta_match.group(1)
                new_meta = meta_text
                if not has_date: new_meta += "\n- **Date:** Unknown"
                if not has_type: new_meta += "\n- **Type:** Unknown"
                if not has_entities: new_meta += "\n- **Entities Involved:** Unknown"
                if not has_source: new_meta += "\n- **Source:** Unknown"
                content = content.replace(meta_text, new_meta)
            else:
                # Insert metadata section after the first heading
                meta_section = "## Event Metadata\n"
                if not has_date: meta_section += "- **Date:** Unknown\n"
                if not has_type: meta_section += "- **Type:** Unknown\n"
                if not has_entities: meta_section += "- **Entities Involved:** Unknown\n"
                if not has_source: meta_section += "- **Source:** Unknown\n"
                
                content = re.sub(r'^(# .+?\n)', f'\\1\n{meta_section}\n', content, count=1)
            
            with open(path, 'w') as fh:
                fh.write(content)

print("Events standardized.")
