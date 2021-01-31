# SoloLeveling

## Overall Description

### Purpose
Management and metrics software to track projects and personal interests. 

### Product Scope 

#### Ticketing system 
Tracks and stores tickets for school, work, and interests. 

#### Metric system
Tracks the time spent and progress for different projects, hobbies, and habits. Display the data on a graph or other easy to read user interface. 

#### Planning System
Allows the user to set goals, milestones, and timelines for a project. 

#### Time tracking
Shows how much time and or tickets I spend on different categories. 

#### Rewards system
Earns coins for each completed task. User can spend the coins for user-defined rewards.

#### Level up system
Each completed task generates exp. Based on the type of task that was completed, the user should gain levels in the matching category. 

#### Coverage
Daily tasks, habits, long term goals, short term goals, school, work.

#### Duration
The idea is to keep this software and maintain it for a lifetime

### Interface Requirements
* Linux terminal until all backend software is completed. 
* Ticketing systems, inputs, outputs will be text based. 
* Graphs will need GUI representation. 
* The backend will interface with a database that stores the tickets and other data. 

### System Features

#### Ticketing System
* Add/Remove Tickets
* Rank difficulties
* The ticket should have a note section
* Label ticket belonging to which goal or milestone
* Label ticket belonging to which category or skillset
* View tickets easily on terminal 
* Daily or regular tickets automatically spawn
* Difficulty ratings Easy, Medium, Hard

#### Metric System
* View the amount of work completed each day
    * The amount of work should be labeled to show the category they are in.
    * Visualize and compare the amount of work each day in a week. 
* Visualize the amount of work completed in a specific category. 
* Growth from different projects and categories over a week or a month.  
* Pie chart to show the work distribution between different categories. 
* Visualize progress of goals
* Visualize habit check-ins. 

#### Planning System
* Can create goals
    * Goal labels can have many milestones
    * Milestones can have many tickets
* Long term goal:  1 month plus
* Short term goal: 1 week plus

#### Rewards System
* Each task will generate coins according to the difficulty level.
* Users can define the reward name and reward price. 
* There should be a one-time reward and repeated rewards 

#### Level Up System
General level Scaling: 
* Each task will generate exp
* Each level should be harder to achieve than the next level. 
* The level should be displayed somewhere in the user interface. 
* Levels should grant titles and effects.

Each category should have its own refinements. 
* Each refinement will be harder to achieve than the next.
* Each refinement should grant titles and effects.

#### (Bonus) Time Tracking System
Time logging completed using logger. The file should be parsed and reported to display the time spent in each category. 

### Product Timeline
The system features will be completed one by one. The due date for the next feature will be updated once the current feature is completed. 
* Aim: complete 5 features within 3 months. 1.7 features a month. 
* Database with python to store tickets or other info: aim: Feb 1st (Feb 3rd deadline)  

 ### Other Nonfunctional Requirements
* Performance Requirement:
    * Tickets will not exceed more than 1k(overestimate) since it is personal use. 
    * Operations should be close to instant as the number of data should be low. 
* Security 
    * Project will be uploaded to github. Preferable the database will be encrypted or not uploaded. 
    * Privacy of the user must be respected. 
* Portability 
    * Nice to have feature is to be able to easily upload and download the project.
