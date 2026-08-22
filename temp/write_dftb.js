const fs = require('fs');
const content = fs.readFileSync('C:/Users/sgg/AppData/Roaming/Tencent/Marvis/User/oAN1i2V14p5-lhhSY365mxizlI-c/workspace/conv_1a0000cc73d_3cc2a0c40aa4/temp/draft_dftb.md', 'utf8');
app.vault.adapter.write('科研Wiki/wiki/concepts/dftb.md', content).then(() => console.log('dftb written'));
