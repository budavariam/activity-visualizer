% Auto-generated: do not edit by hand
\name{activitySelector}

\alias{activitySelector}

\title{ActivitySelector component}

\description{
ActivitySelector lets the user select  the activity from the list of activities given. Has the option to change the year,  that triggers the list to change  out of the scope of this component.
}

\usage{
activitySelector(id=NULL, activityList=NULL, selectedActivity=NULL,
selectedYear=NULL, debugMode=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{activityList}{List of named lists. List of loaded activities}

\item{selectedActivity}{Named list. Data of the selected activity}

\item{selectedYear}{Numeric. Activities are shown from the current selected year}

\item{debugMode}{Logical. Activities are shown from the current selected year}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

