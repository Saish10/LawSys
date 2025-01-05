"""
Utils for accounts.
"""
__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN."

import logging

from accounts.models.invitation import Invitation
from django.db.models import Q

logger = logging.getLogger(__name__)

class InvitationManager:
    """Manager for invitations."""
    def __init__(self, request):
        self.request = request

    def get_invitations(self):
        """Returns a list of invitations."""
        try:
            search = self.request.query_params.get("search")
            role = self.request.query_params.get("role")
            query = Q()
            if search:
                query &= Q(email__icontains=search)
            if role:
                query &= Q(role__id=role)
            return Invitation.objects.select_related("role").filter(query)
        except Exception as e:
            logger.error("Error getting invitations: %s", e, exc_info=True)
            return None

    def get_invitation(self, invitation_id):
        """Returns an invitation by ID."""
        return Invitation.objects.get(invitation_id=invitation_id)
