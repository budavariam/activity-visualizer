# AUTO GENERATED FILE - DO NOT EDIT

activitySelector <- function(id=NULL, activityList=NULL, selectedActivity=NULL, selectedYear=NULL, debugMode=NULL) {
    
    props <- list(id=id, activityList=activityList, selectedActivity=selectedActivity, selectedYear=selectedYear, debugMode=debugMode)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ActivitySelector',
        namespace = 'activity_selector',
        propNames = c('id', 'activityList', 'selectedActivity', 'selectedYear', 'debugMode'),
        package = 'activitySelector'
        )

    structure(component, class = c('dash_component', 'list'))
}
