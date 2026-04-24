<script>
	import projectsData from './projects.json';

	let email = 'studio@kylemcdonald.net';
	let works = projectsData;

	works = works.sort((a, b) => b.year - a.year);
</script>

<main>
	<h1>Kyle McDonald</h1>

	<div class="contacts">
		<a href="mailto:{email}" class="contact contact-email">{email}</a>
		<div class="contact-right">
			<a
				href="https://cf259312.sibforms.com/serve/MUIFAKw5IHoe6UZyqMFlRjjCL1xxVulB-MSI28Y8s1h2Cep5OA24FHHkWhOu6pATgP97B-fdM-kCQoIFzGVgvn-DjKtvGXyL6qnIel8X0wz7ODLEtNOTncE0YgvFG6ssUIEoJOkfSQDbK5yP9aFw8NKsiOo-xFhqzdNnynMp8DpBGM8xByg5Xt2T78RD7VWa623G24QFIMJaTaZG-w=="
				class="contact contact-newsletter"
				>newsletter
				<svg viewBox="0 0 24 24" aria-hidden="true">
					<rect x="3" y="5" width="18" height="14" rx="2" ry="2"></rect>
					<path d="M4 7l8 6 8-6"></path>
				</svg></a
			>
			<a href="https://twitter.com/kcimc" class="contact-icon" aria-label="X" title="X">
				<svg viewBox="0 0 24 24" aria-hidden="true">
					<path d="M4 4l16 16"></path>
					<path d="M20 4L4 20"></path>
				</svg>
			</a>
			<a
				href="https://instagram.com/kcimc"
				class="contact-icon"
				aria-label="Instagram"
				title="Instagram"
			>
				<svg viewBox="0 0 24 24" aria-hidden="true">
					<rect x="3" y="3" width="18" height="18" rx="5" ry="5"></rect>
					<circle cx="12" cy="12" r="4"></circle>
					<circle cx="17.5" cy="6.5" r="1"></circle>
				</svg>
			</a>
		</div>
	</div>

	<div class="section">
		<div class="cell project">
			<h2>Biography</h2>
			<div id="bio">
				<h3>Kyle McDonald</h3>
				is an artist working with code. He crafts interactive installations, sneaky interventions,
				playful websites, workshops, and<a href="http://github.com/kylemcdonald/">toolkits</a> for
				other artists working with code. Exploring possibilities of new technologies: to understand
				how they affect society, to misuse them, and build alternative futures; aiming to share a
				laugh, spark curiosity, create confusion, and share spaces with magical vibes. Working with
				machine learning, computer vision, social and surveillance tech spanning commercial and arts
				spaces. Previously adjunct professor at NYU's <a href="http://itp.nyu.edu">ITP</a>, member
				of <a href="http://fffff.at">F.A.T. Lab</a>, community manager for
				<a href="http://openframeworks.cc">openFrameworks</a>, and artist in residence at
				<a href="http://studioforcreativeinquiry.org/">STUDIO for Creative Inquiry</a>
				at CMU, and <a href="http://ycam.jp">YCAM</a> in Japan. Work commissioned and shown around
				the world, including: the <a href="https://www.vam.ac.uk/">V&A</a>,
				<a href="http://www.ntticc.or.jp/en/">NTT ICC</a>,
				<a href="http://www.aec.at/">Ars Electronica</a>, <a href="http://sonar.es">Sonar</a>,
				<a href="https://todaysart.org/">Todays Art</a>, and
				<a href="https://www.eyebeam.org/">Eyebeam</a>.
			</div>
		</div>

		{#each works as work, i (work)}
			<div class="cell project">
				{#if i == 0}
					<h2>Selected Work</h2>
				{/if}
				<a href={work.links[0].url} name={work.name} target="_blank">
					<img src={`/thumbs/${work.key}.jpg`} alt={work.name} />
				</a>
				<div class="description">
					<h3>
						{work.name}
						<em
							>{work.year}
							{#if work.client}
								for <a href={work.client.url}>{work.client.name}</a>
							{/if}
							{#if work.collaborators}
								{#each work.collaborators as collaborator, j (collaborator)}
									{#if j === 0}
										with
									{:else}
										&nbsp;and
									{/if}
									<a href={collaborator.url}>{collaborator.name}</a>
								{/each}
							{/if}
						</em>
					</h3>
					{@html work.description}
				</div>
				<ul>
					{#each work.links as link}
						<li><a href={link.url}>{link.text}</a></li>
					{/each}
				</ul>
			</div>
		{/each}
	</div>
</main>

<style>
	@import url('style.css');
</style>
