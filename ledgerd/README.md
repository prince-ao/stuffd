# ledgerd

## Problem statement
A small service that holds account balances and moves money between them over HTTP. Clients are unreliable: they time out and retry, and they send the same transfer twice. The process is also unreliable: it gets killed without warning and must come back with the same balances it had. Build the service so that neither kind of unreliability corrupts the books.
