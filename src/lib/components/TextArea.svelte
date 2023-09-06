<script>
	export let name = '';
	export let placeholder = '';
	export let value = '';
	export let mode = true; //True as in light mode, false for dark
	let color = mode ? 'secondary' : 'primary';

    const onInput = e => (value = e.target.value);
</script>


<div>
    <label class={`block mb-2 text-md font-joseph font-meduium text-${color}`} for={name}><slot/></label>
   
    <textarea id={name} name={name} rows="4" cols="50" {placeholder}  on:input={onInput}
    class={`bg-transparent px-3 py-2 mb-3 text-md leading-tight font-joseph font-medium text-${color} border-b border-${color} rounded shadow appearance-none focus:outline-none focus:shadow-outline`}
    />
       
       
      
</div>