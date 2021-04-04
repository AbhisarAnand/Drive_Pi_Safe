# Drive_Pi_Safe
## Inspiration
the BLM situation going on right now and we've seen the impact that it's had on people, specifically speaking people who have an African-American background. Many statistics shown from the Washington Post, CNN, and other reliable websites have interviews that talk about Black people who have been pulled over to the side of the road and been treated unfairly by the cops. Our product will have the ability to solve this issue by being able to automatically begin recording when pulled over, to avoid any issue that may include being treated unfairly and not having proof of it. Since our product automatically records it can be used later as proof to show that the Black person who was pulled over was being treated unfairly. Overall, our group was very passionate about the BLM situation going on right now, and so that's why we decided to create this add-on to our project. The reason we decided to create a product that has the ability to sense drivers on their phone, is because first to ensure the safety of everyone driving at any time, and secondly one of our team members remembered seeing how many people died every year from phone distractions, so we decided we needed to create a viable solution that would be effective, and avoid such terrible incidents so much more often, and we decided to create add-ons so we can make the product more useful with different situations. Lastly, our second add-on that we had was being able to detect if a driver is drowsy, this theme fits in with the main idea of our product, which is to keep a driver and overall safety on the road, and this drowsy detection can allow a driver to pull over if the camera detects that they are sleepy, so that they can get support, etc. Also, our product is a long term solution, people being distracted on their phones will always be an issue, and with our product, it can solve this issue for a long time, it's not a product that comes and goes because this is going to an issue that remains for a long time because humans aren't perfect. 

## What it does
Our product has three main components, two of those components being add-ons as mentioned before. Our product can detect a driver who is on their phone and immediately alert them to get off their phone so it can ensure their safety. It also has an inferred camera that can see in the dark, so even drivers who are driving in the night can't avoid the camera and be alerted to get off their phone. Overall, our product for what it "does" is keeps drivers safe at any time and alerts them if they're doing something wrong. 

## How we built it
We first created a program using open cv, python, HTML, 
We used multithreading, two threads run together, one detects for a person, and another one detects a phone. It runs with a boolean, if both are true, then the second thread plays a sound, which is the warning sound that is played when a person is detected using a phone while driving, and this runs in an infinite loop. 

## Challenges we ran into
We were having a connection error while in the garage, but in the future, you will not be needing connection on the road. The connection was only used to VNC into the program and to start it. meaning that in a real-life scenario no issues with connections would arise and the infinite loop would run smoothly.
We made models that worked, but we quickly realized there were some bugs and were not very accurate, so they eventually turned into drafts and our final product learned from all of our previous mistakes to make it as perfect as possible
A limited amount of time to complete all the tasks, but to counter this issue we used project management, time management, and good teamwork to complete this project in just one day
Our program at first was very choppy because it only ran a few frames per a second (FPS) because of the low computing power of the raspberry pi, we used threading to run two things at once and use the pi in a more efficient way, we also used an Intel Neural Compute Stick 2 which provided extra power in processing.

## Accomplishments that we're proud of
Our very accurate code, that we made together and formatted well
Time management was well thought out
Our teamwork was well synchronized
Project planning allowed all of us to finish our work happily and very well
Our product came out to be very good and accurate 

## What we learned
We learned how serious the issue of texting and driving is, and how 1/6 of people die and get into a car crash and as teenagers, we learned from this terrible stat and we want to make sure we are safe on the road, and that we create a safe environment for everyone else with this product, and also for Black people dealing with discrimination. We improved our technical skills, like making more efficient programs that run at a higher speed, etc. 

## What's next for Drive_Pi_Safe
To help a car stay in its lane, by having a rear camera, we also want to add a camera that goes on the back of the car that's connected to the steering wheel camera, and this camera will have the ability to detect speeding cars behind. We also want to add a front camera to the steering wheel pi so it is looking out at the road, and this camera will have the ability to detect any potholes, dead animals, and anything else that's blocking the road ahead of the driver that he man is not able to see. All these abilities if added will enhance the safety and security of the car and the person driving the car. Also for the pi at the steering wheel, we want to add an ability with Machine Learning algorithm's so that our pi can hear glass breaking of a car, and immediately send a text to the owner of the pi that glass at their car has been shattered. 

## Youtube Demo Video:
[link](https://www.youtube.com/watch?v=L4ThmJuHLz4)

## Our Website:
[link](https://drivepisafe.abhisar.repl.co/)

## Contributors
<a href="https://github.com/AbhisarAnand/Drive_Pi_Safe/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AbhisarAnand/Drive_Pi_Safe" />
</a>
