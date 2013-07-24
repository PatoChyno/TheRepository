<%inherit file="default.mako" />
<%block name="page_content">
<div>
Showing tasks for user ${user}
</div>
% for task in tasks:
    <div> ${task.task} assigned to ${task.user} <div>
% endfor
</%block>
