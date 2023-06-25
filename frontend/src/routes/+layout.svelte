<script>
	import '../app.css';
	import Menu from '../components/Menu.svelte';
	import Workspace from '../components/Workspace.svelte';
</script>

<Menu />
<Workspace>
	<slot />
</Workspace>
