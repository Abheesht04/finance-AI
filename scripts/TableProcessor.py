class TableProcessor:

    def process(self, document):

        for page in document.get_pages():

            for section in page.get_sections():

                if section.get_name() != "TABLE":

                    continue

                #
                # Future:
                #
                # Split into logical rows
                # Merge wrapped descriptions
                # Detect columns
                #

                pass
