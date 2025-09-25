# DATA603 A2  |  DOB: 05/07/2002

import argparse, re, pdfplumber

def clean_text(t):
    import re
    t = re.sub(r'[ \t]+', ' ', t or '')
    t = re.sub(r'\n{3,}', '\n\n', t)
    return t.strip() + "\n"

def grab(pdf_path, pdf_1idx_start, book_page_start, out_txt, n=10):
    start_pdf_page_1idx = pdf_1idx_start + (book_page_start - 1)
    with pdfplumber.open(pdf_path) as pdf, open(out_txt, "w", encoding="utf-8") as f:
        for i in range(n):
            p = start_pdf_page_1idx + i
            if p < 1 or p > len(pdf.pages): break
            text = pdf.pages[p-1].extract_text(x_tolerance=2, y_tolerance=2)
            f.write(clean_text(text))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--book_start_in_pdf", type=int, required=True)  # 1-indexed viewer page where Book 7 begins
    ap.add_argument("--day", type=int, required=True)   # birth day 1..31
    ap.add_argument("--year", type=int, required=True)  # e.g., 2002
    args = ap.parse_args()

    # file1 from birth date
    grab(args.pdf, args.book_start_in_pdf, args.day, "file1.txt", 10)

    # file2 from year rule: 2002 -> 102
    yy = args.year % 100
    p_year = (100 + yy) if args.year >= 2000 else (yy or 1)
    grab(args.pdf, args.book_start_in_pdf, p_year, "file2.txt", 10)

    print("Created file1.txt and file2.txt")
