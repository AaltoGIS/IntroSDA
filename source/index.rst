.. figure:: img/ISDA_banner.png

**Introduction to Spatial Data Analysis** -course introduces you to different analysis approaches and methods of spatio-statistical analysis, geostatistics, map algebra
and geovisual analysis. After the course, you can identify appropriate analysis approaches for different geospatial tasks,
and describe data needs and suitable methods for the given analysis process. You can discuss the strengths and limitations of the methods.
The course has been developed at the Department of Built Environment, Aalto University, Finland, and the materials are openly available for anyone interested.

.. .. important::
    Notice that the **course starts only on the 3rd week of 1st teaching period, i.e. the first lecture is on Tuesday 16th September**.

Learning objectives
-------------------

After completing this course, you should:

- understand the typical data analysis workflow
- understand the basics of geostatistics and the associated terminology and mathematical principles
- understand the basic principles of map overlay and map algebra
- understand the principles of graph theory and network analysis
- understand the basic principles of spatio-temporal multivariate analysis
- be able to apply the previous concepts to different geographical problems using Python programming language and desktop GIS

Prerequirements
---------------

Before taking this course, it is required to know the basics of Python programming as well as GIS.

**Python basics:** If you are new to Python, or would like to refresh your Python skills, we recommend to go through the Part 1 materials (Chapters 1-4) on the open online book,
`Introduction to Python for Geographic Data Analysis <https://pythongis.org/>`__ by Tenkanen, Heikinheimo & Whipp (2025). In case you want to earn credits (5 ECTS) while learning the basics of Python,
we recommend to take a course called Geo-Python at University of Helsinki which is available at `geo-python.github.io <http://geo-python.github.io/>`__.
You can `enroll to this course via Sisu <https://sisu.aalto.fi/student/courseunit/otm-745028e1-2a87-4eb1-abce-ee708626fcb6/brochure>`__ (i.e. if you are a student at Aalto University).
The course runs in the first teaching period (starting in September).

Supporting material
-------------------

**GIS with Python:** During this course, we will learn various GIS and spatial analysis techniques using Python programming. To support your learning,
we recommend to go through the Part 2 materials (Chapters 5-8) on the open online book, `Introduction to Python for Geographic Data Analysis <https://pythongis.org/>`__.
In addition, we will cover topics from `Geographic Data Science with Python <https://geographicdata.science/book/intro.html>`__ by Rey, Arribas-Bel & Wolf (2023) which we recommend
as supporting reading.

In case you want to earn credits (5 ECTS) while learning the GIS related techniques with Python, we recommend to take a course Automating GIS-processes (GEOG-329-2) at University of Helsinki which is available at `autogis.github.io <https://autogis.github.io/>`__.
You can `enroll to this course via Sisu <https://sisu.aalto.fi/student/courseunit/otm-0dd8eff5-bd05-4bcf-982d-7d960506c1ba/brochure>`__ (i.e. if you are a student at Aalto University).
The course runs in the second teaching period (starting at the end of October).

.. admonition:: Help improving the materials

    **This is version 2.**

    The course was given for the very first time in its current form in 2024, meaning that the content of the course is likely to change and
    improve after each time the course is given (all versions will be available). By being a fully open
    educational resource, **you can also help making the course better**.
    If you find any errors, typos, or other problems, please help, by suggesting an edit in GitHub. You can do this easily by clicking
    ``suggest edit`` under the GitHub icon located at
    the top-right on each page:

    .. image:: img/suggest_edit.png
       :width: 130px

    |
    If you have good ideas about what should be taught, i.e. what methods, interesting datasets or literature should be introduced
    during the course, you can suggest and bring your ideas forward by `raising an issue in GitHub <https://github.com/AaltoGIS/IntroSDA/issues/new>`__.


Course format
-------------

The majority of this course will be spent in front of a computer writing code with the Python language.
The course consists of lectures, tutorials and weekly exercises. The exercises will focus on
applying the introduced methods to given geographical problems.

Most exercises in this course involve real world examples and data. For each exercise, you may be asked to
submit the Python codes you have written, output figures and answers to related questions. You are encouraged to
discuss and work together with other students while working on the weekly exercises.

.. admonition:: Aalto University students

    The Introduction to Spatial Data Analysis -course is part of the
    `Master's Programme of Geoinformatics at Aalto University <https://www.aalto.fi/en/study-options/masters-programme-in-geoinformatics>`__
    under the course code ``GIS-E1130``.

Program
-------

The course includes two lectures per week and is held at the Aalto University starting in the first teaching period.
Topics per week are listed below. Please note that this web page is updated each week before the given lesson:

.. list-table::
    :widths: 1 8
    :header-rows: 1
    :stub-columns: 1
    :align: left

    * - Week
      - Themes
    * - 1
      - - Course overview and practicalities
        - Introduction to spatial analysis
        - Potential and pitfalls of spatial data
    * - 2
      - - Spatial data model
        - Point pattern analysis
        - Density and clustering
    * - 3
      - - The concept of neighborhood and spatial analysis
        - Spatial effects: dependency and heterogeneity
        - Spatial autocorrelation
    * - 4
      - - Analysis of spatial field data
        - Map overlay & algebra
        - Surface analysis
    * - 5
      - - Spatial network analysis
        - Graph problems and shortest path algorithms
        - Optimization & centrality
    * - 6
      - - Spatial data structures
        - Spatial algorithms
        - Computational geometry: Topology and spatial relationships
    * - 7
      - - Spatial data indexing
        - Spatial index
        - Spatial data management and databases
    * - 8
      - - Geostatistics
        - Spatial interpolation (IDW+Kriging)
    * - 9
      - - Cartography and Map User Interfaces
        - Visual analytics
    * - 10
      - - Introduction to GeoAI

|

Contents
--------

.. toctree::
    :maxdepth: 1
    :caption: Course information

    course-info/course-info
    course-info/learning-goals
    course-info/grading
    course-info/course-environment-components
    course-info/slack-usage
    course-info/License-terms
    course-info/attribution
    course-info/resources
    .. course-info/installing-miniconda


.. toctree::
    :maxdepth: 1
    :caption: Exercises

    exercises/exercise-1
    exercises/exercise-2
    .. exercises/exercise-3
    .. exercises/exercise-4
    .. exercises/exercise-5

.. toctree::
    :maxdepth: 1
    :caption: Tutorials

    .. tutorials/git-basics
    .. tutorials/intro-to-python-geostack.ipynb
    .. tutorials/spatial_network_analysis.ipynb


.. toctree::
    :maxdepth: 1
    :caption: Week 1

    lessons/L1/overview
    lessons/L1/introduction
    lessons/L1/introduction-to-spatial-analysis
    lessons/L1/spatial-data-potential-and-pitfalls

.. toctree::
   :maxdepth: 1
   :caption: Week 2

   lessons/L2/overview
   lessons/L2/spatial-data-model
   lessons/L2/point-pattern-analysis

.. toctree::
    :maxdepth: 1
    :caption: Week 3

    lessons/L3/overview
    lessons/L3/spatial-effects
    lessons/L3/spatial-autocorrelation

.. toctree::
    :maxdepth: 1
    :caption: Week 4

    lessons/L4/overview
    lessons/L4/spatial-field-data-and-map-algebra
    lessons/L4/surface-analysis


.. toctree::
    :maxdepth: 1
    :caption: Week 5

    .. lessons/L5/overview
    .. lessons/L5/spatial-network-analysis
    .. lessons/L5/graph-problems-and-algorithms



.. toctree::
    :maxdepth: 1
    :caption: Week 6

    .. lessons/L6/overview
    .. lessons/L6/spatial-data-structures
    .. lessons/L6/voronoi-and-delanay

.. toctree::
    :maxdepth: 1
    :caption: Week 7

    .. lessons/L7/overview
    .. lessons/L7/spatial-indexing
    .. lessons/L7/spatial-data-management-and-databases

.. toctree::
    :maxdepth: 1
    :caption: Week 8

    .. lessons/L8/overview
    .. lessons/L8/geostatistics-kriging


.. toctree::
    :maxdepth: 1
    :caption: Week 9

    .. lessons/L9/overview
    .. lessons/L9/cartography-map-user-interfaces
    .. lessons/L9/visual-analytics

.. toctree::
    :maxdepth: 1
    :caption: Week 10

    .. lessons/L10/overview
    .. lessons/L10/multivariate-spatial-analysis
    .. lessons/L10/intro-to-GeoAI


