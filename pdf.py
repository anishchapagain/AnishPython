import pdfplumber

# Balance sheet with Projectd and Audited columns (two year)
pdf_tech = pdfplumber.open("data\\tech_innovator.pdf")

total_pages = len(pdf_tech.pages)
contents=""
i=0
while i < total_pages:
    page = i
    print(f"Processing Page: {page}")
    texts = pdf_tech.pages[page].extract_text_simple()
    contents += texts
    i+=1
    # # tables = pdf_tech.find_tables()
    # # print(tables)
    # page = pdf_tech.pages[1]
    # print(page)
    # print(page.chars[100])
    # print(f"{'-'*10}")
    # page_tables = page.find_tables()
    # print(page_tables)
    # print(page_tables[0].extract())

print(len(contents))
print(contents)

