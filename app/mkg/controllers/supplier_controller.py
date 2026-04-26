from app.database import db
from app.mkg.model.supplier_model import Supplier


class SupplierController:

    def create_supplier(self, data):
        name = data.get("name")
        contact = data.get("contact")

        if not name:
            return {"status": "error", "message": "Name required"}, 400

        supplier = Supplier(name=name, contact=contact)
        db.session.add(supplier)
        db.session.commit()

        return {"status": "success", "data": {"id": supplier.id, "name": name}}, 201

    def get_suppliers(self):
        suppliers = Supplier.query.all()

        return {
            "status": "success",
            "data": [{"id": s.id, "name": s.name} for s in suppliers]
        }, 200

    def delete_supplier(self, supplier_id):
        supplier = Supplier.query.get(supplier_id)

        if not supplier:
            return {"status": "error", "message": "Not found"}, 404

        db.session.delete(supplier)
        db.session.commit()

        return {"status": "success", "message": "Deleted"}, 200