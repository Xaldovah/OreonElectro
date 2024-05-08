from django.test import TestCase
from .models import Discount, Coupon, Promotion
from django.utils import timezone
from datetime import timedelta

class DiscountModelTests(TestCase):
    def test_create_discount(self):
        discount = Discount.objects.create(name='Test Discount', percentage=10.0)
        self.assertEqual(str(discount), "Test Discount - 10.0%")


class CouponModelTests(TestCase):
    def test_is_valid(self):
        discount = Discount.objects.create(name='Test Discount', percentage=10.0)
        now = timezone.now()
        coupon = Coupon.objects.create(code='TEST10', discount=discount, valid_from=now - timedelta(days=1), valid_to=now + timedelta(days=1))
        self.assertTrue(coupon.is_valid())


class PromotionModelTests(TestCase):
    def test_is_active(self):
        discount = Discount.objects.create(name='Test Discount', percentage=10.0)
        now = timezone.now()
        promotion = Promotion.objects.create(title='Test Promotion', description='Description', discount=discount, valid_from=now - timedelta(days=1), valid_to=now + timedelta(days=1))
        self.assertTrue(promotion.is_active())
