<%inherit file="default.mako" />
<%block name="page_content">
% for task in tasks:
    <div> ${task.task} assigned to ${task.user} </div>
% endfor
</%block>
