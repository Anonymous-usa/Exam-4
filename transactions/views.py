from rest_framework import generics, permissions, filters
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['description', 'category']
    ordering_fields = ['date', 'amount']

    def get_queryset(self):
        user = self.request.user
        queryset = Transaction.objects.filter(user=user)

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        transaction_type = self.request.query_params.get('transaction_type')
        if transaction_type in ['income', 'expense']:
            queryset = queryset.filter(transaction_type=transaction_type)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

  