from scripts.document_section import DocumentSection


class SectionProcessor:

    def process(self, document):

        for page in document.get_pages():

            self._process_page(page)

    # ---------------------------------------------------

    def _process_page(self, page):

        current_sections = {}

        #
        # We keep multiple sections alive at once.
        #

        for row in page.get_layout_rows():

            columns = row.get_columns()

            #
            # Visit every column separately
            #

            for column in columns:

                text = column.get_text().strip()

                #
                # HEADER
                #

                if "INVOICE" == text:

                    section = DocumentSection()
                    section.set_name("HEADER")

                    page.add_section(section)

                    current_sections["HEADER"] = section

                    continue

                #
                # BILL TO
                #

                if text.startswith("Bill To"):

                    section = DocumentSection()
                    section.set_name("BILL_TO")

                    page.add_section(section)

                    current_sections["LEFT"] = section

                    section.add_row(column)

                    continue

                #
                # SHIP TO
                #

                if text.startswith("Ship To"):

                    section = DocumentSection()
                    section.set_name("SHIP_TO")

                    page.add_section(section)

                    current_sections["CENTER"] = section

                    section.add_row(column)

                    continue

                #
                # TABLE
                #

                if text == "Item":

                    section = DocumentSection()
                    section.set_name("TABLE")

                    page.add_section(section)

                    current_sections["TABLE"] = section

                    section.add_row(column)

                    continue

                #
                # TOTALS
                #

                if text.startswith("Subtotal"):

                    section = DocumentSection()
                    section.set_name("TOTALS")

                    page.add_section(section)

                    current_sections["RIGHT"] = section

                    section.add_row(column)

                    continue

                #
                # NOTES
                #

                if text.startswith("Notes"):

                    section = DocumentSection()
                    section.set_name("NOTES")

                    page.add_section(section)

                    current_sections["LEFT"] = section

                    section.add_row(column)

                    continue

                #
                # TERMS
                #

                if text.startswith("Terms"):

                    section = DocumentSection()
                    section.set_name("TERMS")

                    page.add_section(section)

                    current_sections["LEFT"] = section

                    section.add_row(column)

                    continue

                #
                # Continue active sections
                #

                if len(columns) == 1:

                    #
                    # Left side
                    #

                    if "LEFT" in current_sections:

                        current_sections["LEFT"].add_row(column)

                    #
                    # Table
                    #

                    if "TABLE" in current_sections:

                        current_sections["TABLE"].add_row(column)

                elif len(columns) == 2:

                    #
                    # Left column

                    if "LEFT" in current_sections:

                        current_sections["LEFT"].add_row(columns[0])

                    #
                    # Right column

                    if "CENTER" in current_sections:

                        current_sections["CENTER"].add_row(columns[1])
