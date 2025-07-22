#!/bin/bash

# Script to regenerate Python SDK documentation from AsteroidClient class
# This script extracts methods from the class and generates Mintlify accordion components

set -e

# Configuration
CLIENT_FILE="src/asteroid_odyssey/client.py"
DOCS_FILE="../docs/sdk/python.mdx"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Regenerating Python SDK documentation...${NC}"

# Check if source file exists
if [ ! -f "$CLIENT_FILE" ]; then
    echo -e "${RED}❌ Error: Client file not found at $CLIENT_FILE${NC}"
    exit 1
fi

# Check if docs file exists
if [ ! -f "$DOCS_FILE" ]; then
    echo -e "${RED}❌ Error: Documentation file not found at $DOCS_FILE${NC}"
    exit 1
fi

# Function to extract method information using Python
extract_method_info() {
    python3 -c "
import re
import ast
import sys

class MethodExtractor(ast.NodeVisitor):
    def __init__(self):
        self.methods = []
        self.in_asteroid_client = False
        
    def visit_ClassDef(self, node):
        if node.name == 'AsteroidClient':
            self.in_asteroid_client = True
            self.generic_visit(node)
            self.in_asteroid_client = False
    
    def visit_FunctionDef(self, node):
        if self.in_asteroid_client and not node.name.startswith('_'):
            # Extract method info
            method_info = {
                'name': node.name,
                'docstring': ast.get_docstring(node) or '',
                'args': [],
                'lineno': node.lineno
            }
            
            # Extract arguments
            for arg in node.args.args:
                if arg.arg != 'self':
                    method_info['args'].append(arg.arg)
            
            self.methods.append(method_info)
    
    def parse_docstring(self, docstring):
        if not docstring:
            return {
                'description': 'No description available.',
                'short_desc': 'Method description',
                'args': {},
                'returns': 'None',
                'raises': 'None',
                'example': ''
            }
        
        lines = docstring.strip().split('\n')
        parsed = {
            'description': '',
            'short_desc': 'Method description',
            'args': {},
            'returns': 'None',
            'raises': 'None',
            'example': ''
        }
        
        current_section = 'description'
        description_lines = []
        current_arg = None
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            if line.startswith('Args:'):
                current_section = 'args'
            elif line.startswith('Returns:'):
                current_section = 'returns'
            elif line.startswith('Raises:'):
                current_section = 'raises'
            elif line.startswith('Example:'):
                current_section = 'example'
            elif current_section == 'description' and line:
                description_lines.append(line)
            elif current_section == 'args':
                if line and ':' in line and not line.startswith(' '):
                    # New argument
                    arg_match = re.match(r'\s*(\w+):\s*(.*)', line)
                    if arg_match:
                        current_arg = arg_match.group(1)
                        parsed['args'][current_arg] = arg_match.group(2)
                elif line and current_arg and line.startswith('  '):
                    # Continuation of current argument description
                    parsed['args'][current_arg] += ' ' + line.strip()
            elif current_section == 'returns' and line:
                if parsed['returns'] == 'None':
                    parsed['returns'] = line
                else:
                    parsed['returns'] += ' ' + line
            elif current_section == 'raises' and line:
                if parsed['raises'] == 'None':
                    parsed['raises'] = line
                else:
                    parsed['raises'] += '\n' + line
            elif current_section == 'example' and line:
                parsed['example'] += line + '\n'
            
            i += 1
        
        full_desc = ' '.join(description_lines) if description_lines else 'No description available.'
        parsed['description'] = full_desc
        
        # Extract short description (first sentence)
        sentences = full_desc.split('.')
        if sentences and sentences[0].strip():
            parsed['short_desc'] = sentences[0].strip()
        else:
            parsed['short_desc'] = 'Method description'
            
        return parsed

# Read and parse the file
try:
    with open('$CLIENT_FILE', 'r') as f:
        source = f.read()
    
    tree = ast.parse(source)
    extractor = MethodExtractor()
    extractor.visit(tree)
    
    # Generate documentation for each method
    for method in extractor.methods:
        parsed_doc = extractor.parse_docstring(method['docstring'])
        
        # Generate method signature
        args_str = ', '.join(method['args']) if method['args'] else ''
        signature = f\"{method['name']}({args_str})\"
        
        print(f\"METHOD_START:{method['name']}\")
        print(f\"SIGNATURE:{signature}\")
        print(f\"SHORT_DESC:{parsed_doc['short_desc']}\")
        print(f\"DESCRIPTION:{parsed_doc['description']}\")
        print(f\"ARGS:{len(method['args'])}\")
        for arg in method['args']:
            arg_desc = parsed_doc['args'].get(arg, 'No description available')
            print(f\"ARG:{arg}:{arg_desc}\")
        print(f\"RETURNS:{parsed_doc['returns']}\")
        print(f\"RAISES:{parsed_doc['raises']}\")
        print(f\"EXAMPLE_START\")
        print(parsed_doc['example'].strip())
        print(f\"EXAMPLE_END\")
        print(f\"METHOD_END\")
        
except Exception as e:
    print(f'ERROR: {e}', file=sys.stderr)
    sys.exit(1)
"
}

# Extract method information
echo -e "${YELLOW}📋 Extracting method information...${NC}"
METHOD_DATA=$(extract_method_info)

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Error extracting method information${NC}"
    echo "$METHOD_DATA"
    exit 1
fi

# Generate accordion documentation
generate_accordions() {
    current_method=""
    short_desc=""
    in_example=false
    echo "$METHOD_DATA" | while IFS= read -r line; do
        if [[ $line == METHOD_START:* ]]; then
            current_method="${line#METHOD_START:}"
            
        elif [[ $line == SIGNATURE:* ]]; then
            signature="${line#SIGNATURE:}"
            
        elif [[ $line == SHORT_DESC:* ]]; then
            short_desc="${line#SHORT_DESC:}"
            echo "<Accordion title=\"${current_method}() - ${short_desc}\">"
            echo ""
            
        elif [[ $line == DESCRIPTION:* ]]; then
            description="${line#DESCRIPTION:}"
            echo "$description"
            echo ""
            
        elif [[ $line == ARGS:* ]]; then
            arg_count="${line#ARGS:}"
            if [ "$arg_count" -gt 0 ]; then
                echo "**Parameters:**"
                echo ""
            fi
            
        elif [[ $line == ARG:* ]]; then
            arg_info="${line#ARG:}"
            arg_name="${arg_info%%:*}"
            arg_desc="${arg_info#*:}"
            echo "- \`$arg_name\`: $arg_desc"
            
        elif [[ $line == RETURNS:* ]]; then
            returns="${line#RETURNS:}"
            if [ "$returns" != "None" ]; then
                echo ""
                echo "**Returns:** $returns"
            fi
            
        elif [[ $line == RAISES:* ]]; then
            raises="${line#RAISES:}"
            if [ "$raises" != "None" ]; then
                echo ""
                echo "**Raises:**"
                echo ""
                echo "$raises" | sed 's/^/- /'
            fi
            
        elif [[ $line == EXAMPLE_START ]]; then
            echo ""
            echo "\`\`\`python"
            in_example=true
            
        elif [[ $line == EXAMPLE_END ]]; then
            echo "\`\`\`"
            in_example=false
            
        elif [ "$in_example" = true ]; then
            echo "$line"
            
        elif [[ $line == METHOD_END ]]; then
            echo "</Accordion>"
            echo ""
        fi
    done
}

# Generate the new accordion content
echo -e "${YELLOW}📝 Generating accordion documentation...${NC}"
ACCORDION_CONTENT=$(generate_accordions)

# Find the accordion section in the docs file and replace it
echo -e "${YELLOW}🔄 Updating documentation file...${NC}"

# Create a backup
cp "$DOCS_FILE" "${DOCS_FILE}.backup"

# Use Python to replace the accordion section
python3 -c "
import re

# Read the current docs file
with open('$DOCS_FILE', 'r') as f:
    content = f.read()

# The new accordion content
accordion_content = '''$ACCORDION_CONTENT'''

# Look for the Core Methods accordion group specifically
core_methods_pattern = r'(## Core Methods\s*<AccordionGroup>\s*)(.*?)(\s*</AccordionGroup>)'

def replace_accordion(match):
    start_tag = match.group(1)
    end_tag = match.group(3)
    return start_tag + accordion_content + end_tag

new_content = re.sub(core_methods_pattern, replace_accordion, content, flags=re.DOTALL)

# Write back to file
with open('$DOCS_FILE', 'w') as f:
    f.write(new_content)

print('Documentation updated successfully!')
"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Documentation successfully regenerated!${NC}"
    echo -e "${GREEN}📍 Updated file: $DOCS_FILE${NC}"
    echo -e "${YELLOW}💾 Backup created: ${DOCS_FILE}.backup${NC}"
else
    echo -e "${RED}❌ Error updating documentation file${NC}"
    # Restore backup
    mv "${DOCS_FILE}.backup" "$DOCS_FILE"
    exit 1
fi

echo -e "${GREEN}🎉 Python SDK documentation regeneration complete!${NC}"
echo ""
echo -e "${YELLOW}📋 Summary:${NC}"
echo "• Extracted methods from AsteroidClient class"
echo "• Generated Mintlify accordion components"
echo "• Updated $DOCS_FILE with new documentation" 
echo "• Created backup at ${DOCS_FILE}.backup"
echo ""
echo -e "${GREEN}🚀 Documentation is ready for review!${NC}" 