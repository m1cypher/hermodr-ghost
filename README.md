<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/m1cypher/hermodr-ghost">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Hermodr Ghost Application</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/m1cypher/hermodr-ghost"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/m1cypher/hermodr-ghost">View Demo</a>
    ·
    <a href="https://github.com/m1cypher/hermodr-ghost/issues">Report Bug</a>
    ·
    <a href="https://github.com/m1cypher/hermodr-ghost/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://boydsbar.xyz/oppenheimer)

I currently write reviews for movies, TV shows, and book for my own fun. However, I have been publishing them to a blog for the past year. However, this has become faily tedious and I want to be able to automate as much as I can. Currently I use [Obsidian](https://obsidian.md) to write the reviews and then they are manually published on a [Ghost blog](https://ghost.org) that I selfhost on a VPS. After writing the review, I copy and paste it to the blog and then setup a publish date and email. This works without issue, but I hate the back and forth.

This project should accomplish the following with some thoughts below each step:

1) Scan repository of my backed up obsidian notes. (This might be better suited for something like gitlab or gitea, but for now will be a script to practice python skills and transferability for other users.)
2) If the repository has new notes that meet certain requirements (Either is labeled as completed or no additional edits in 72 hours), stag to publish to ghost.
3) Publish notes to Ghost blog using API.
4) Scehdule weekly email to go out with excerpt and score for the review (Right now, each review has its own email. This really isn't the best as I personally hate getting blaseted by emails from people and would prefer a weekly roll up to see if anything is worth reading. So this weekly email will have an excert from each review and then the score).

I will be building this with OOP in mind.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* Python

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Download the git project.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

This project assumes a couple things.

1) You use obsidian to save your blogs.
2) You use Obsidian Git to save your vault to Github.
3) You are using Ghost to host your blogs.

  ```sh
  git clone https://github.com/m1cypher/hermodr-ghost.git
  ```

### Installation

1. Modify permissions for the scripts

```sh
cd /hermodr-ghost
chmod +x *.sh
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

After working prototype is completed, you can check out the wiki page for documentation.

_For more examples, please refer to the [Documentation](https://github.com/m1cypher/hermodr-ghost/wiki)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

* [ ] Create repository scanning script
* [ ] Create DB to store the published blogs.
* [ ] Create Blog publicion script
* [ ] Create Email Publication script

See the [open issues](https://github.com/m1cypher/hermodr-ghost/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Your Name - [@mimircyber](https://twitter.com/mimircyber) - <info@mimircyber.com>

Project Link: [https://github.com/m1cypher/hermodr-ghost](https://github.com/m1cypher/hermodr-ghost)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/m1cypher/hermodr-ghost.svg?style=for-the-badge
[contributors-url]: https://github.com/m1cypher/hermodr-ghost/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/m1cypher/hermodr-ghost.svg?style=for-the-badge
[forks-url]: https://github.com/m1cypher/hermodr-ghost/network/members
[stars-shield]: https://img.shields.io/github/stars/m1cypher/hermodr-ghost.svg?style=for-the-badge
[stars-url]: https://github.com/m1cypher/hermodr-ghost/stargazers
[issues-shield]: https://img.shields.io/github/issues/m1cypher/hermodr-ghost.svg?style=for-the-badge
[issues-url]: https://github.com/m1cypher/hermodr-ghost/issues
[license-shield]: https://img.shields.io/github/license/m1cypher/hermodr-ghost.svg?style=for-the-badge
[license-url]: https://github.com/m1cypher/hermodr-ghost/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/garrett-e-boyd
[product-screenshot]: images/screenshot.png
