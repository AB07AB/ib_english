const textTypes = {
  Advertisement: [
    'A sleek and minimalistic print ad for a new smartphone, highlighting its eco-friendly production.',
    'A loud, colourful commercial showcasing a cleaning product that removes tough stains in seconds.'
  ],
  'Blog Post': [
    "An influencer's reflective post about sustainable fashion choices.",
    'A personal journal entry recounting a cross-country road trip adventure.'
  ],
  Speech: [
    "A politician's campaign speech focused on education reform.",
    'A motivational talk encouraging resilience during setbacks.'
  ],
  'News Report': [
    'A factual report about a recent scientific discovery and its potential impact on health.',
    'An investigative article exploring the rise of urban farming.'
  ],
  Cartoon: [
    'A single-panel comic illustrating the irony of online privacy in the age of social media.',
    'A satirical graphic highlighting consumerism during holiday sales.'
  ]
};

const difficulties = {
  Easy: 'Identify the target audience and primary purpose of this text. Discuss one persuasive technique used.',
  Medium: 'Analyze how the structure and tone contribute to the text\'s effectiveness. Identify hidden implications.',
  Hard: 'Examine subtle stylistic devices and intertextual references. Reflect on cultural or ideological messages that might not be evident at first glance.'
};

const newChallengeButton = document.querySelector('#new-challenge');
const card = document.querySelector('#challenge-card');
const textTypeEl = document.querySelector('#text-type');
const promptEl = document.querySelector('#prompt');
const difficultyLabel = document.querySelector('#difficulty-label');
const difficultyDescription = document.querySelector('#difficulty-description');
const responseInput = document.querySelector('#response-input');

function getRandomItem(array) {
  const index = Math.floor(Math.random() * array.length);
  return array[index];
}

function getRandomKey(obj) {
  const keys = Object.keys(obj);
  return getRandomItem(keys);
}

function generateChallenge() {
  const textType = getRandomKey(textTypes);
  const prompt = getRandomItem(textTypes[textType]);
  const difficulty = getRandomKey(difficulties);

  textTypeEl.textContent = `Text Type: ${textType}`;
  promptEl.textContent = prompt;
  difficultyLabel.textContent = difficulty;
  difficultyDescription.textContent = difficulties[difficulty];

  responseInput.value = '';
  card.classList.remove('hidden');
  responseInput.focus({ preventScroll: true });
}

newChallengeButton.addEventListener('click', generateChallenge);

document.addEventListener('DOMContentLoaded', () => {
  generateChallenge();
});
