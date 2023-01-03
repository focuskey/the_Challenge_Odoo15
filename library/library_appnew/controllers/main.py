from odoo import http


class Books(http.Controller):
    @http.route("/library/books")
    def list(self, **kwargs):
        Book = http.request.env['library.book']
        books = Book.search([])
        return http.request.render(
            "carpet_w.book_list_template",
            {"books": books}
        )