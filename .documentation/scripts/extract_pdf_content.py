#!/usr/bin/env python3
"""
PDF Text Extraction Script for AI Workflow Analysis Documentation
Extracts text content from PDF analysis files and organizes into markdown documentation.
"""

import pdfplumber
import os
from pathlib import Path
import json
from datetime import datetime

# Configuration
SOURCE_DIR = Path(".documentation/source-pdfs")
OUTPUT_DIR = Path(".documentation/ai-workflow-analysis/extracted-content")
PDF_FILES = [
    "AI workflow analysis.pdf",
    "AI workflow analysis (1).pdf",
    "AI workflow analysis (2).pdf",
    "AI workflow analysis (3).pdf",
    "AI workflow analysis (4).pdf",
    "AI workflow analysis (5).pdf",
    "AI workflow analysis (6).pdf",
    "AI workflow analysis (7).pdf",
    "AI workflow analysis (8).pdf",
]


def extract_pdf_text(pdf_path):
    """Extract text content from PDF file."""
    try:
        text_content = []
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                if text:
                    text_content.append({
                        "page": page_num,
                        "text": text
                    })
        return text_content
    except Exception as e:
        print(f"Error extracting {pdf_path}: {e}")
        return None


def organize_content_by_sections(text_content):
    """Organize extracted content into logical sections."""
    # This is a basic organization - can be enhanced with NLP
    sections = {
        "overview": [],
        "findings": [],
        "analysis": [],
        "metrics": [],
        "recommendations": [],
        "other": []
    }
    
    # Basic keyword-based organization
    keywords = {
        "overview": ["overview", "summary", "introduction", "executive"],
        "findings": ["finding", "result", "discovery", "key"],
        "analysis": ["analysis", "examine", "evaluate", "assess"],
        "metrics": ["metric", "measure", "score", "percentage", "rate"],
        "recommendations": ["recommend", "suggest", "should", "improve"]
    }
    
    for page_data in text_content:
        text = page_data["text"].lower()
        categorized = False
        
        for section, keywords_list in keywords.items():
            if any(keyword in text for keyword in keywords_list):
                sections[section].append(page_data)
                categorized = True
                break
        
        if not categorized:
            sections["other"].append(page_data)
    
    return sections


def save_extracted_content(pdf_name, content, sections):
    """Save extracted content to markdown files."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Save full text
    full_text_path = OUTPUT_DIR / f"{pdf_name}_full_text.txt"
    with open(full_text_path, "w", encoding="utf-8") as f:
        for page_data in content:
            f.write(f"\n--- Page {page_data['page']} ---\n")
            f.write(page_data["text"])
    
    # Save organized sections
    sections_path = OUTPUT_DIR / f"{pdf_name}_sections.md"
    with open(sections_path, "w", encoding="utf-8") as f:
        f.write(f"# Extracted Content: {pdf_name}\n\n")
        f.write(f"**Extraction Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for section_name, section_content in sections.items():
            if section_content:
                f.write(f"\n## {section_name.upper()}\n\n")
                for page_data in section_content:
                    f.write(f"### Page {page_data['page']}\n\n")
                    f.write(page_data["text"])
                    f.write("\n\n---\n\n")
    
    # Save metadata
    metadata = {
        "pdf_name": pdf_name,
        "extraction_date": datetime.now().isoformat(),
        "total_pages": len(content),
        "sections": {k: len(v) for k, v in sections.items()}
    }
    
    metadata_path = OUTPUT_DIR / f"{pdf_name}_metadata.json"
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    
    return full_text_path, sections_path, metadata_path


def main():
    """Main extraction process."""
    print("Starting PDF text extraction...")
    print(f"Source directory: {SOURCE_DIR.absolute()}")
    print(f"Output directory: {OUTPUT_DIR.absolute()}\n")
    
    # Check if pdfplumber is available
    try:
        import pdfplumber
    except ImportError:
        print("ERROR: pdfplumber not installed.")
        print("Install with: pip install pdfplumber")
        return
    
    # Process each PDF
    results = []
    for pdf_file in PDF_FILES:
        pdf_path = SOURCE_DIR / pdf_file
        
        if not pdf_path.exists():
            print(f"⚠️  Skipping {pdf_file} - file not found")
            continue
        
        print(f"📄 Processing: {pdf_file}")
        
        # Extract text
        content = extract_pdf_text(pdf_path)
        
        if content:
            # Organize content
            sections = organize_content_by_sections(content)
            
            # Save content
            full_text, sections_file, metadata = save_extracted_content(
                pdf_file.replace(".pdf", ""),
                content,
                sections
            )
            
            results.append({
                "pdf": pdf_file,
                "pages": len(content),
                "full_text": str(full_text),
                "sections": str(sections_file),
                "metadata": str(metadata)
            })
            
            print(f"   ✅ Extracted {len(content)} pages")
            print(f"   📝 Saved to: {sections_file}")
        else:
            print(f"   ❌ Failed to extract content")
    
    # Save extraction summary
    summary_path = OUTPUT_DIR / "extraction_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump({
            "extraction_date": datetime.now().isoformat(),
            "total_pdfs": len(results),
            "results": results
        }, f, indent=2)
    
    print(f"\n✅ Extraction complete!")
    print(f"📊 Summary saved to: {summary_path}")
    print(f"\nNext steps:")
    print(f"1. Review extracted content in: {OUTPUT_DIR}")
    print(f"2. Organize content into documentation sections")
    print(f"3. Populate markdown documentation files")


if __name__ == "__main__":
    main()

