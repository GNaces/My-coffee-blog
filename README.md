![Mr CoffeePH Logo](static/images/mrcoffee.jpg)
# Mr CoffeePH Blog

Live deployment for the app here https://coffee-lover-blog-500caab782a2.herokuapp.com/

## Introduction

Mr CoffeePH is a comprehensive blog platform dedicated to coffee culture that aims to engage coffee fans of all skill levels. This website is a digital environment where users may explore coffee-related content, tips, and tales, ranging from the complexities of brewing procedures to worldwide coffee trends. The goal is to create a vibrant community of coffee enthusiasts who can easily discover, interact with, and share their enthusiasm for coffee. This blog is not intended to replace Mr CoffeePH's official website https://mrcoffeeph.com/

Mr CoffeePH is built on the Django framework and leverages Django's powerful backend features to provide a scalable, secure, and high-performance platform. Few of the features how Mr CoffeePH delivers a streamlined, engaging experience:

      - Create comments to a post.
      - Read posts.
      - Update posts, either their own (using the edit post option) or others' (by commenting and/or like them).
      - Delete only posts that they created themselves.

The blog's UI is responsive and mobile-friendly, ensuring that users enjoy the best possible experience whether they access it via desktop, tablet, or smartphone. The layout adapts dynamically to screen sizes, providing for seamless navigation, readability, and interaction across all devices.

Users are urged to register accounts in order to develop a sense of community and a more customized experience. Users have access to exclusive interactive features such as the option to "like" blog posts and comment on posts after completing a simple sign-up process.

Registered users can show their enthusiasm for articles by "liking" them. This helps to highlight popular contents on the page, increasing engagement and discussion.
Prompted Login for Interaction: Mr CoffeePH features a nice notification system for users who have not yet logged in.

When an unregistered user tries to interact, they are asked to log in or create an account using the link provided. This small nudge simultaneously improves security and encourages user registration, resulting in a more connected user experience.

An admin dashboard, accessible to moderators and admins, enables effective content control. The Django admin interface makes it simple to publish new posts, manage users, and evaluate user interactions, ensuring that the blog remains relevant and interesting.


## Project Planning

The major goal of this project was to create a simple, user-friendly platform that provides an engaging environment for individuals to exchange and debate coffee-related tales, tips, and content. Key characteristics allow users to:

1. Register for a Personal Account
      - Permission-based access promotes a more controlled and good forum experience, hence creating a welcoming environment.

2. Create comments to a posts using their account name.
      - Allowing individuals to write their own comments and promotes self-expression and meaningful discussions about coffee.

3. Manage posted comments with the option to edit or delete.
      - The platform allows users to change or remove their comments, giving them more control over their personal thoughts on the posts.

4. Read, like, and comment on page's posts.
      - Interaction features such as liking and commenting let users form community ties and interact actively.

5. Administrator Control Over All Content
      - Admins have control and regulates "waiting for approval" comments as appropriate, thereby promoting a safe and friendly atmosphere.


The user stories for this project can be viewed [here](https://github.com/users/GNaces/projects/5)

### Models

Three models were utilized for this project. The Post model controls user postings, the Comment model manages user comments, and the Like model keeps track of who liked the post.

![Post Model](assets/images/post_model.jpg)

![Comment Model](assets/images/comment_model.jpg)

![Like Model](assets/images/like_model.jpg)


## Project Management

GitHub's KanBan board were utilized to organize the process. [Mr CoffeePH Workflow](https://github.com/users/GNaces/projects/5)

KanBan it provides a flexible and agile way to manage my workload. It is extremely useful for solitary tasks; it improved the efficiency of managing workload through its accessible depiction, resulting in increased production.

The board enabled me to simply move stories through the business delivery lifecycle of To Do -> In Progress -> Done.

## Features

### Welcome to Mr CoffeePH Blog

When users start the app, they are greeted with a landing page consisting of blog posts, which they may peruse even without an account. 
Users who do not yet have an account will see a sign up option in the navbar, allowing them to create one.

![Index Page](assets/images/index_page.jpg)

Users who have an account will see a navbar with the options to logout and a status that shows them they are signed in, as well as the ability to see user posts and post likes and comments.

![User Index Page](assets/images/index_page_user.jpg)

### Create An Account

Users can create a personal user account, which allows them to create their own posts. 

![Sign Up Page](assets/images/sign_up.jpg)

### Create Comments and Like on a Blog Post

Once a user's account is set up, they are given more choices such as commenting and liking posts. 

![Create Comment](assets/images/create_comments.jpg)

![Like Post](assets/images/like_post.jpg)

