import re
from typing import List, Tuple


def extract_code_blocks(
        markdown_text: str,
        languages: List[str] = ['javascript', 'jsx', 'css', 'python', 'html','ts','astro','js'],
        include_markers: bool = False
) -> List[Tuple[str, str]]:
    """
    Extracts code blocks and their associated filenames from markdown text for specified languages.
    Args:
        markdown_text (str): The text containing code blocks.
        languages (List[str]): A list of languages to extract. Defaults to ['javascript', 'jsx', 'css'].
        include_markers (bool): Whether to include the code block markers. Defaults to False.
    Returns:
        List[Tuple[str, str]]: A list of tuples, each containing the filename and the extracted code block.
    """
    # Normalize newlines
    markdown_text = markdown_text.replace('\r\n', '\n').replace('\r', '\n')
    
    # Find all code blocks
    blocks = []
    current_pos = 0
    while True:
        # Find start of code block
        start = markdown_text.find('```', current_pos)
        if start == -1:
            break
            
        # Find language identifier
        newline = markdown_text.find('\n', start)
        if newline == -1:
            break
            
        lang = markdown_text[start+3:newline].strip()
        if lang not in languages:
            current_pos = start + 3
            continue
            
        # Find end of code block
        end = markdown_text.find('```', newline)
        while end != -1:
            # Check if this is really the end (not part of content)
            block_content = markdown_text[newline+1:end]
            if '```' not in block_content:
                break
            end = markdown_text.find('```', end + 3)
            
        if end == -1:
            # Try to find end with newlines
            end = markdown_text.find('\n```', newline)
            if end == -1:
                # If no end marker is found, use the rest of the text
                end = len(markdown_text)
            else:
                end += 1  # Skip the newline
            
        # Extract block
        block = markdown_text[newline+1:end].strip()
        blocks.append((lang, block))
        current_pos = end + 3
    
    extracted_blocks = []
    for lang, block in blocks:
        filename = f'unknown.{lang}'
        code = block
        if lang in languages:
            lines = block.split('\n')
            if not lines:
                continue
                
            first_line = lines[0].strip()
            if first_line.startswith('//'):
                # Extract filename from // comment
                filename_match = first_line.lstrip('/ ').strip()
                if filename_match:
                    filename = filename_match
                    code = '\n'.join(lines[1:]).strip()
            elif first_line.startswith('/*'):
                # Extract filename from /* --- */ comment
                filename_match = re.match(r'\/\*\s*(.+?)\s*\*\/', first_line)
                if filename_match:
                    filename = filename_match.group(1).strip()
                    code = '\n'.join(lines[1:]).strip()
            elif first_line.startswith('#'):
                # Extract filename from # comment
                filename_match = first_line.lstrip('# ').strip()
                if filename_match:
                    filename = filename_match
                    code = '\n'.join(lines[1:]).strip()
                    
            # Remove ./ prefix from filename if present
            if filename.startswith('./'):
                filename = filename[2:]
                    
        if include_markers:
            code = f"```{lang}\n{code}\n```"
        extracted_blocks.append((filename, code))
    return extracted_blocks


def extract_solution(llm_response: str) -> List[Tuple[str, str]]:
    """
    Extracts a list of file paths and code file contents from the LLM's response.
    Args:
        llm_response (str): The response containing code blocks.
    Returns:
        List[Tuple[str, str]]: A list of tuples (file_path, file_content).
    """
    extracted_blocks = extract_code_blocks(llm_response)
    result = []
    for filename, code in extracted_blocks:
        # Handle CSS file path
        if filename == 'unknown.css':
            filename = 'src/styles/App.css'
        result.append((filename, code))
    return result
