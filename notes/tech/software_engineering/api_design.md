# API Design

* Design end-to-end workflows instead of single APIs.
* Don't put too many classes directly under the same path for importing. It is hard for the user to auto-complete the class name since there would be too many candidates.
* The keywords in constructor should be accessible with the instance. (i.e. the constructor keywords should also be attributes or properties)
* If the parent class and the sub class share some args, the required arguments should be documented again in the sub class even they are the same. The arguments in kwargs can be not documented.
For the ones not required and not in the kwargs, we should also document them even they are repeated in some other classes.
* In docstrings of a class, use Args or Arguments to specify the args of init. Use Attributes to specify the attributes which are not init args but publicly accessible.
* It is not a good practice for the user to provide a list, whose length is required to be a specific number. The user may easily miss some of the elements and got an error.
* Do not use acronym for any API related things exposed to the users unless it is a really well-known acronym.
* If the subclass doesn't support some kwarg, it should raise an error when user use it, instead of ignore them silently.
* When type checking boolean, should be clear whether 0 and 1 are considered valid or not.
