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
#         organization_name=pricing.organization.name
#         print(organization_name)
#         item_type = pricing.item.type  # Fetching item_type from related Item object
#         print(item_type)
#         base_distance = pricing.base_distance_in_km
#         base_price = pricing.fix_price
#         per_km_price = pricing.km_price

#         if total_distance <= base_distance:
#             total_price = base_price
#         else:
#             extra_distance = total_distance - base_distance
#             total_price = base_price + extra_distance * per_km_price

#         return total_price

from .models import Pricing

class PriceCalculator:
    @staticmethod
    def calculate_price(zone, organization_id, total_distance, item_type):
        pricing = Pricing.objects.filter(
            organization_id=organization_id,
            zone=zone,
            item__type=item_type  # Filtering based on item type
        ).first()
        print(item_type)
        if not pricing:
            return None

        base_distance = pricing.base_distance_in_km
        base_price = pricing.fix_price
        per_km_price = pricing.km_price

        if total_distance <= base_distance:
            total_price = base_price
        else:
            extra_distance = total_distance - base_distance
            total_price = base_price + extra_distance * per_km_price

        return total_price
