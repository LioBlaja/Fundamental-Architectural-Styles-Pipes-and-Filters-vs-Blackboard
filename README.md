# Fundamental-Architectural-Styles-Pipes-and-Filters-vs-Blackboard



Design and Architecture of Complex Software Systems (DACSS)

Back to lab assignment list
Assignment 1: Fundamental Architectural Styles: Pipes-and-Filters vs Blackboard
Pipes-and-Filters and Blackboard are two architectural styles defined by the different patterns of interaction at runtime between the components of a system. The goal of this assignment is to understand the differences and similarities between these two fundamental architectural styles and to study how the choice of a particular architectural style affects the solution of a problem.

You will design and implement two different versions of the same system (automatic review moderator bot), according to the two different architectural styles. The detailed description of the requirements for the system follows in a section below.

Each student will complete two different implementations: one implementation using pure Pipes and Filters vs another implementation using pure Blackboard architectural styles.

This assignment puts together two lab sessions (corresponding weeks 2 and 3). The duration of this assignment is 2 weeks (results should be presented no later than week 4). Delays bring a penalty of 1 point for each weeek of delay after the deadline.

General grading policy: Grades reflect your individual knowledge and contribution. Each student must complete and present their own solutions. Fraud attempts will be assigned 0(zero) points. Not doing the assignment is assigned by default 4 points.

References:

    Lecture notes of weeks 2 and 3
    POSA1 - chap.2.2 (for Pipes and Filters and Blackboard)
    David Garlan, Mary Shaw, An Introduction to Software Architecture, Technical Report Carnegie-Mellon University, no CMU-CS-94-166, online . (subsections 3.1 - Pipes and Filters, 3.3 - Event-based, 3.5 - Repositories and the exemples in section 4) 

Detailed description
Your company develops an Automatic Reviews Moderator bot (well, a simplified mock version only). It can be used as a filtering and labeling preprocessor in online systems handling user reviews of the products of an online shop. Actually, you will maintain a software product line for the product family of review moderators, because you have various clients requiring small variations in the review moderator features.

The incoming messages are simulated by lines of text, containing tokens separated by comma. Their format is: username, productname, reviewtext, attachment. The attachment is a substring that mocks an attached image. We assume that all lines have a valid format. You are able to support following features:

    elliminate messages from users who have not bought the reviewed product (username is not found in a list of buyers of the product).
    elliminate messages that contain profanities in the review text (mock implementation: reviewtext substring does not contain @#$%)
    elliminate messages that contain political propaganda in the review text (mock implementation: reviewtext does not contain +++ or ---)
    resize pictures in attachment if they are too large(mock implementation: if the attachment substring representing the attached picture contains uppercase letters, transform them in lowercase).
    remove competitor website links from the text of the message (mock implementation: elliminate substring http from review text)
    analyze sentiment of the review (positive, negative or neutral) and attach a classification (mock implementation: reviewtext contains more uppercase letters or more lowercase letters determine pozitive or negative sentiment. Append a +, - or = sign at the end of the reviewtext) 

Your clients will include various online shops, each requiring a customized version of the reviews moderator bot to suit their specific preferences. For example: One client may accept pictures but require them to be resized if they are too large. Another client just does not care about pictures. One client may accept reviews from any user, while another may require reviews only from certified buyers of the product.

For example, consider that the required features are: elliminate messages with profanities, accept only reviews from buyers of the product, resize pictures, and determine sentiments. If the registered acquisitions are: John â€“ Laptop; Mary â€“ Phone; Ann - Book, then:

For the input:

John, Laptop, ok, PICTURE
Mary, Phone, @#$%), IMAGE
Peter, Phone, GREAT, ManyPictures
Ann, Book, So GOOD, Image

The output will be:

John, Laptop, ok-, picture
Ann, Book, So GOOD+, image

In both architectural versions, you will implement a collection of specific reusable components handling the various features. It should be easy for your company to reuse them in order to quickly assemble a new custom version of the automatic reviews moderator.

Between certain steps (tasks), there are logical order relationships, while other steps can be done in any order. As a general rule, tasks that eliminate messages should be performed before tasks that transform messages (it makes no sense to first resize pictures and then identify that the message contains profanities, which will cause the message to be eliminated). However, there are no preferred orderings between the different types of eliminator tasks.

In a Pipes-and-Filters style, it is the responsibility of the assembler to ensure that the components (the filters) are placed in a valid order in a linear pipeline. An example of a valid pipeline for the aforementioned example is:

In a Blackboard style, all components have access to the messages in various processing stages (stored on the blackboard) and it is the responsibility of each component (the knowledge sources) to decide when it is a right moment to perform its task on a message.

For each of the two investigated architectural styles (Pipes-Filters and Blackboard):

    design and implement the collection of reusable components handling the various filtering tasks
    for each style, assemble at least two different systems, according to different client preferences, in order to show the reusability of your components and of your design. 

Optional development

Investigate the impact of concurrency on the two architectural styles: Concurrent Pipes-and-Filters vs Concurrent Blackboard.

Implement versions of the automatic review moderator where transformation tasks are executed concurrently (For Pipes-and-Filters: Filters are active components working in parallel; For Blackboard: Knowledge Sources are active components working in parallel). Pay attention to syncronization !

Additional Resources: APD/PDA lecture slides on Java threads and parallelism

In order to observe relevant behavioural differences, make each processing task to have a configurable duration and experiment with different values for the duration. Have an input of at least N=100 messages and compare the time when their processing is finished, in both cases. For each style, assemble at least two different systems. Find relevant scenarios where each architectural style's strengths and weaknesses are most apparent.

Deadline and Grading: This optional part has a HARD deadline in week 5 and brings 1 Bonus point. The Bonus poimt is granted for a complete fulfillment of the requirements which comprise: the implementations of concurrent PipesFilters and Blackboard, the experiments and measurements, and the discussion and conclusion of the comparison. 
