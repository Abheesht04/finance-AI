class ContextBuilder:

    def build(self, document, invoice):

        context = {}

        context["document"] = self._document(document)
        context["invoice"] = self._invoice(invoice)

        return context

    # -------------------------------------------------

    def _document(self, document):

        metadata = document.get_metadata()

        return {

            "pages": document.get_page_count(),

            "metadata": {

                "title": metadata.get_title(),

                "author": metadata.get_author(),

                "creator": metadata.get_creator(),

                "producer": metadata.get_producer(),

                "creation_date": metadata.get_creation_date(),

                "modification_date": metadata.get_modification_date()

            }

        }

    # -------------------------------------------------

    def _invoice(self, invoice):

        data = {}

        # ---------------------------------------------
        # Header
        # ---------------------------------------------

        header = invoice.get_header()
        vendor = invoice.get_vendor()
        totals = invoice.get_totals()

        data["vendor"] = vendor.get_name()

        data["invoice_type"] = header.get_invoice_type()

        data["invoice_number"] = header.get_invoice_number()

        data["invoice_date"] = header.get_invoice_date()

        # ---------------------------------------------
        # Totals
        # ---------------------------------------------

        data["totals"] = {

            "subtotal": str(totals.get_subtotal()),

            "shipping": str(totals.get_shipping()),

            "balance_due": str(totals.get_balance_due()),

            "total": str(totals.get_total())

        }

        # ---------------------------------------------
        # Items
        # ---------------------------------------------

        data["items"] = []

        for item in invoice.get_items().get_all():

            data["items"].append({

                "description": item.get_description(),

                "sku": item.get_sku(),

                "category": item.get_category(),

                "quantity": item.get_quantity(),

                "unit_price": str(item.unit_price()),

                "line_total": str(item.line_total()),

                "discount": {

                    "name": item.discount().get_name(),

                    "percentage": item.discount().get_percentage(),

                    "amount": str(item.discount().amount())

                },

                "tax": {

                    "name": item.tax().get_name(),

                    "percentage": item.tax().get_percentage(),

                    "amount": str(item.tax().amount())

                }

            })

        return data
