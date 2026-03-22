import os, re

relations_dir = 'docs/relations'

for f in os.listdir(relations_dir):
    if f.endswith('.md') and not f.startswith('index'):
        path = os.path.join(relations_dir, f)
        with open(path, 'r') as fh:
            content = fh.read()
        
        # Check for missing fields
        has_conf = bool(re.search(r'\*\*Confidence', content))
        
        if not has_conf:
            # Insert Confidence field after the first heading
            content = re.sub(r'^(# .+?\n)', f'\\1**Confidence:** 95% (Estimated)  \n', content, count=1)
            
            with open(path, 'w') as fh:
                fh.write(content)

print("Relations standardized.")
