##################important note##############################
##we can use item_id insted of item_type using below code we have to change view.py slightly where we can get item_id insted of item_type 




# from .models import Pricing

# class PriceCalculator:
#     @staticmethod
#     def calculate_price(zone, organization_id, total_distance, item_id):
#         pricing = Pricing.objects.filter(
#             organization_id=organization_id,
#             zone=zone,
#             item_id=item_id  # Changed to item_id
#         ).first()

#         if not pricing:
#             return None
       
#         item_type = pricing.item.type  # Fetching item_type from related Item object
#         base_distance = pricing.base_distance_in_km
#         base_price = pricing.fix_price
#         per_km_price = pricing.km_price

#         if item_type=="non_perishable":
#             per_km_price = 1

#         if total_distance <= base_distance:
#             total_price = base_price
#         else:
#             extra_distance = total_distance - base_distance
#             total_price = base_price + extra_distance * per_km_price

#         return total_price


#code for item_type

from decimal import Decimal
from .models import Pricing

class PriceCalculator:
    @staticmethod
    def calculate_price(zone, organization_id, total_distance, item_type):
        pricing = Pricing.objects.filter(
            organization_id=organization_id,
            zone=zone,
            item__type=item_type  # Filtering based on item type
        ).first()

        if not pricing:
            return None

        base_distance = pricing.base_distance_in_km
        base_price = pricing.fix_price
        per_km_price = pricing.km_price

        # Uncomment and correct the conditions for different item types
        per_km_price = Decimal('1.5')

        if item_type == "non_perishable":
            per_km_price = Decimal('1')

        if total_distance <= base_distance:
            total_price = base_price
        else:
            extra_distance = total_distance - base_distance
            total_price = base_price + extra_distance * per_km_price

        return total_price