<%inherit file="default.mako" />
<%block name="title">News trends</%block>
<%block name="page_content">
	<div>
		<form method="POST" action="${request.route_path('stats')}">
			<div>
				<label for="input_word">Zadaj slovo:</label>
				<input name="word" id="input_word">
			</div>
			<div>
				<input name="submit_word" value="Najdi" type="submit">
			</div>
		</form>
	</div>
</%block>
