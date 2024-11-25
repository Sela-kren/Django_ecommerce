from django.core.management.base import BaseCommand
from store.models import Product

class Command(BaseCommand):
    help = 'Seed the products table with predefined skincare products data'

    def handle(self, *args, **kwargs):
        # Clear existing products for clean seeding (optional)
        Product.objects.all().delete()

        # Predefined skincare products
        products = [
            {"name": "Neutrogena Hydro Boost Water Gel", "description": "A lightweight gel moisturizer with hyaluronic acid.", "price": 19.99, "stock": 50, "image_url": "https://example.com/images/neutrogena_hydro_boost.jpg"},
            {"name": "CeraVe Hydrating Facial Cleanser", "description": "A gentle, non-foaming cleanser for normal to dry skin.", "price": 14.99, "stock": 75, "image_url": "https://example.com/images/cerave_hydrating_cleanser.jpg"},
            {"name": "Olay Regenerist Micro-Sculpting Cream", "description": "Anti-aging cream that helps visibly reduce fine lines and wrinkles.", "price": 24.99, "stock": 40, "image_url": "https://example.com/images/olay_micro_sculpting_cream.jpg"},
            {"name": "The Ordinary Niacinamide 10% + Zinc 1%", "description": "A serum designed to target blemishes, congestion, and sebum production.", "price": 6.99, "stock": 100, "image_url": "https://example.com/images/ordinary_niacinamide_zinc.jpg"},
            {"name": "Drunk Elephant T.L.C. Sukari Babyfacial", "description": "An AHA/BHA mask that exfoliates to reveal smoother, brighter skin.", "price": 80.00, "stock": 30, "image_url": "https://example.com/images/drunk_elephant_babyfacial.jpg"},
            {"name": "CeraVe AM Facial Moisturizing Lotion SPF 30", "description": "Moisturizer with broad-spectrum SPF 30 for daily protection.", "price": 18.99, "stock": 60, "image_url": "https://example.com/images/cerave_am_lotion_spf30.jpg"},
            {"name": "La Roche-Posay Anthelios Melt-in Sunscreen Milk SPF 60", "description": "A sunscreen offering broad-spectrum protection and a non-greasy finish.", "price": 36.00, "stock": 45, "image_url": "https://example.com/images/la_roche_posay_sunscreen.jpg"},
            {"name": "Clinique Moisture Surge 72-Hour Auto-Replenishing Hydrator", "description": "Oil-free, gel-cream for instant moisture.", "price": 39.50, "stock": 80, "image_url": "https://example.com/images/clinique_moisture_surge.jpg"},
            {"name": "Tatcha The Dewy Skin Cream", "description": "A rich, dewy moisturizer that promotes a glowing, hydrated complexion.", "price": 68.00, "stock": 25, "image_url": "https://example.com/images/tatcha_dewy_skin.jpg"},
            {"name": "Kiehl’s Calendula Herbal Extract Alcohol-Free Toner", "description": "A soothing toner that helps reduce redness and inflammation.", "price": 45.00, "stock": 70, "image_url": "https://example.com/images/kiehls_calendula_toner.jpg"},
            {"name": "L’Oréal Paris Revitalift Bright Reveal Brightening Peel Pads", "description": "Exfoliating pads with glycolic acid to improve skin texture and radiance.", "price": 17.99, "stock": 120, "image_url": "https://example.com/images/loreal_revitalift_peel_pads.jpg"},
            {"name": "Paula’s Choice Skin Perfecting 2% BHA Liquid Exfoliant", "description": "A salicylic acid exfoliant that clears pores and reduces blemishes.", "price": 29.99, "stock": 90, "image_url": "https://example.com/images/paulas_choice_bha_exfoliant.jpg"},
            {"name": "Neutrogena Ultra Sheer Dry-Touch Sunscreen SPF 100+", "description": "High SPF sunscreen that provides broad-spectrum protection.", "price": 8.99, "stock": 150, "image_url": "https://example.com/images/neutrogena_ultra_sheer_sunscreen.jpg"},
            {"name": "The Ordinary Hyaluronic Acid 2% + B5", "description": "A hydrating serum that delivers moisture to the skin.", "price": 6.80, "stock": 110, "image_url": "https://example.com/images/ordinary_hyaluronic_acid.jpg"},
            {"name": "Fresh Rose Face Mask", "description": "Hydrating and soothing mask infused with real rose petals.", "price": 62.00, "stock": 20, "image_url": "https://example.com/images/fresh_rose_face_mask.jpg"},
            {"name": "Olay Luminous Tone Perfecting Cream", "description": "Moisturizer designed to brighten and even out skin tone.", "price": 28.00, "stock": 50, "image_url": "https://example.com/images/olay_luminous_tone.jpg"},
            {"name": "Drunk Elephant C-Firma Day Serum", "description": "A potent vitamin C serum that fights signs of aging.", "price": 78.00, "stock": 30, "image_url": "https://example.com/images/drunk_elephant_c_firma.jpg"},
            {"name": "Biossance Squalane + Vitamin C Rose Oil", "description": "A nourishing oil that brightens and hydrates the skin.", "price": 72.00, "stock": 40, "image_url": "https://example.com/images/biossance_squalane_vitamin_c.jpg"},
            {"name": "Murad AHA/BHA Exfoliating Cleanser", "description": "A dual-action exfoliating cleanser with AHA and BHA.", "price": 40.00, "stock": 60, "image_url": "https://example.com/images/murad_aha_bha_cleanser.jpg"},
            {"name": "Tata Harper Clarifying Cleanser", "description": "A clarifying cleanser that helps reduce oil and prevent acne.", "price": 58.00, "stock": 30, "image_url": "https://example.com/images/tata_harper_clarifying_cleanser.jpg"},
        ]

        # Create each predefined product
        for product in products:
            Product.objects.create(
                name=product['name'],
                description=product['description'],
                price=product['price'],
                stock=product['stock'],
                image_url=product['image_url']
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded skincare products'))
