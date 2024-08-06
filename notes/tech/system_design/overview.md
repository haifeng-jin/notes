Database replication modes:

Master-Slave Replication: One primary database (master) accepts writes, and multiple secondary databases (slaves) replicate the data. This ensures that data is consistent across all databases, but may introduce some latency.

Multi-Master Replication: All databases accept writes and replicate data with each other. This ensures high availability and low latency, but can be more complex to manage.


Considerations:

Cache invalidation: How will you invalidate cache entries when data is updated in one of the databases?


How to interview?

* Clarify the requirements.
* Give the design and explain the reasons behind it.
* Give the potential issues and tradeoffs.
