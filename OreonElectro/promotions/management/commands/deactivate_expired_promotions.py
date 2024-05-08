from django.core.management.base import BaseCommand
from django.utils import timezone
from promotions.models import Coupon, Promotion


class Command(BaseCommand):
    help = 'Deactivate expired coupons and promotions'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        expired_coupons = Coupon.objects.filter(valid_to__lt=now, active=True)
        expired_promotions = Promotion.objects.filter(valid_to__lt=now, active=True)

        expired_coupons.update(active=False)
        expired_promotions.update(active=False)

        self.stdout.write(self.style.SUCCESS(f'Successfully deactivated {expired_coupons.count()} expired coupons and {expired_promotions.count()} expired promotions.'))
