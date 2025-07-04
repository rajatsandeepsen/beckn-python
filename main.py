from beckn import Transaction

client = Transaction.ApiClient(
    configuration=Transaction.Configuration(
        host="https://api.example.com",
        api_key="example",
    )
)

data = Transaction.BecknApplicationPlatformBAPApi(
        client=client
    ).on_search_post(
        Transaction.OnSearch(
            context=Transaction.OnSearchContext(), 
            message=Transaction.OnSearchMessage()
        )
    )

print(data)