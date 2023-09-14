<script>
	export let name = '';
	export let placeholder = '';
	export let type = 'text';
	export let value = '';
	export let mode = true; //True as in light mode, false for dark
	let color = mode ? 'secondary' : 'primary';

	function typeAction(node) {
		node.type = type;
	}
    const onInput = e => (value = e.target.value);
</script>

<div class="w-max">
	<label class={`block mb-2 text-sm font-joseph font-meduium text-${color}`} for={name}>
		<slot />
	</label>
	<input
		use:typeAction
		{value}
        on:input={onInput}
		class={`bg-transparent px-3 py-2 mb-3 text-sm leading-tight font-joseph font-medium text-${color} border-b border-${color} rounded shadow appearance-none focus:outline-none focus:shadow-outline`}
		id={name}
		{placeholder}
	/>
</div>
