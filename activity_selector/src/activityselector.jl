
module ActivitySelector
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("activityselector.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "activity_selector",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "activity_selector.min.js",
    external_url = "https://unpkg.com/activity_selector@0.0.1/activity_selector/activity_selector.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "activity_selector.min.js.map",
    external_url = "https://unpkg.com/activity_selector@0.0.1/activity_selector/activity_selector.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
