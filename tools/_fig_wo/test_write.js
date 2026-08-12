#!/usr/bin/env node
// Generate all crystal-structures subpages

const fs = require('fs');
const path = require('path');

// Use forward slashes and explicit path
const BASE = 'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki';
const FIG_DIR = path.join(BASE, 'wiki', 'figures');

// Verify directory exists
console.log('FIG_DIR:', FIG_DIR);
console.log('FIG_DIR exists:', fs.existsSync(FIG_DIR));

// Load groups
const spGroups = JSON.parse(fs.readFileSync(path.join(BASE, 'tools', '_fig_wo', 'sp_groups.json'), 'utf8'));
console.log('Loaded groups:', Object.keys(spGroups).map(k => `${k}=${spGroups[k].length}`).join(', '));

// Verify we can write
const testPath = path.join(FIG_DIR, 'write_test.tmp');
fs.writeFileSync(testPath, 'test\n', 'utf8');
console.log('Write test:', fs.existsSync(testPath) ? 'PASS' : 'FAIL');
fs.unlinkSync(testPath);
