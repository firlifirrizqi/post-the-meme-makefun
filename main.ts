// Entry for the make.fun bounty "Post the Meme, Win the Feed" (Node 22, stdlib only).
// The entry is the X post itself: POST.json names the post, and this program
// copies POST.json from the repository root to /output/POST.json, where the
// gate reads it. That is all the program has to do.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });
// Validate POST.json before copying: it must exist, parse as JSON, and name
// a real X post URL — a leftover placeholder must never be handed to the gate.
const postPath = join(BOT_DIR, 'POST.json');
const post = JSON.parse(readFileSync(postPath, 'utf8'));
if (
  typeof post.url !== 'string' ||
  !/^https:\/\/(x\.com|twitter\.com)\/\S+\/status\/\d+$/.test(post.url) ||
  /\/status\/0+$/.test(post.url)
) {
  console.error(`POST.json at ${postPath} does not name a valid X post URL.`);
  process.exit(1);
}
copyFileSync(postPath, join(OUTPUT_DIR, 'POST.json'));
