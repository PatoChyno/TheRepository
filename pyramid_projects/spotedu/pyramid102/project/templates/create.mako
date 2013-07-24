<%inherit file="default.mako" />
<%block name="page_content">
	<form action="${request.route_path('create_task')}" method="POST">
		<div>
			<label for="task">Task</label>
			<input type="text" name="task" required/>
		</div>
		<div>
            <label>User</label>
            <input type="text" name="user_id" required/>
		</div>
        <button type="submit" class="submit-form">vytvor task</button>
    </form>
</%block>
