# Generated by Django 3.2.6 on 2021-08-17 06:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import djstripe.enums
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0012_alter_transfer_schema_change_3"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usagerecord",
            name="description",
        ),
        migrations.RemoveField(
            model_name="usagerecord",
            name="metadata",
        ),
        migrations.AddField(
            model_name="usagerecord",
            name="action",
            field=djstripe.fields.StripeEnumField(
                default="increment",
                enum=djstripe.enums.UsageAction,
                help_text="When using increment the specified quantity will be added to the usage at the specified timestamp. The set action will overwrite the usage quantity at that timestamp. If the subscription has billing thresholds, increment is the only allowed value.",
                max_length=9,
            ),
        ),
        migrations.AddField(
            model_name="usagerecord",
            name="timestamp",
            field=djstripe.fields.StripeDateTimeField(
                blank=True,
                help_text="The timestamp for the usage event. This timestamp must be within the current billing period of the subscription of the provided subscription_item.",
                null=True,
            ),
        ),
        migrations.CreateModel(
            name="UsageRecordSummary",
            fields=[
                ("djstripe_created", models.DateTimeField(auto_now_add=True)),
                ("djstripe_updated", models.DateTimeField(auto_now=True)),
                (
                    "djstripe_id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("id", djstripe.fields.StripeIdField(max_length=255, unique=True)),
                (
                    "livemode",
                    models.BooleanField(
                        blank=True,
                        default=None,
                        help_text="Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.",
                        null=True,
                    ),
                ),
                (
                    "created",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="The datetime this object was created in stripe.",
                        null=True,
                    ),
                ),
                (
                    "period",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="Subscription Billing period for the SubscriptionItem",
                        null=True,
                    ),
                ),
                (
                    "period_end",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="End of the Subscription Billing period for the SubscriptionItem",
                        null=True,
                    ),
                ),
                (
                    "period_start",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="Start of the Subscription Billing period for the SubscriptionItem",
                        null=True,
                    ),
                ),
                (
                    "total_usage",
                    models.PositiveIntegerField(
                        help_text="The quantity of the plan to which the customer should be subscribed."
                    ),
                ),
                (
                    "djstripe_owner_account",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        help_text="The Stripe Account this object belongs to.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.account",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
                (
                    "invoice",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="usage_record_summaries",
                        to="djstripe.invoice",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
                (
                    "subscription_item",
                    djstripe.fields.StripeForeignKey(
                        help_text="The subscription item this usage record contains data for.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="usage_record_summaries",
                        to="djstripe.subscriptionitem",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
            ],
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
    ]
