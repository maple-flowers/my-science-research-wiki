---
metatable: true
vaultPath: 科研Wiki/raw/note
outType: md
searchTag: ""
searchCodePro1: ""
searchCodePro2: ""
searchYear: 2026年
searchMonth: 3月
searchFinish: All
searchPublicationTitle: All
sortRule: importDate
obsidianUIMode: preview
---

```dataviewjs
/*YAML
# 通用参数
metatable: true
vaultPath: Notes
outType: md
searchTag: 
searchCodePro1:
searchCodePro2:
#筛选参数
searchYear: 全部年
searchMonth: 全部月
searchFinish: All
searchPublicationTitle: All
sortRule: importDate
*/
///基础定义
///时长
let TimeList = {};
let timeCount = 0;
TimeList["Time0"] = new Date().getTime();
function TimeMonitor() {
  timeCount += 1;
  TimeList["Time" + timeCount] = new Date().getTime();
  console.log("Step " + timeCount.toString() + " --> " + (TimeList["Time" + timeCount] - TimeList["Time" + (timeCount - 1)]).toString() + " ms");
}
let title = [];
let titlevalue = "outputs = outputs.map((b) => [";
///---可修改范围---///

title.push("文献笔记");
//titlevalue += "'<div style=\"width: 15em\">'+"; // 修改数字变更栏宽
titlevalue += "b.file.link";
//titlevalue += "+'</div>'"; // 不变更栏宽不要添加
titlevalue += ",";
title.push("中文标题");
//titlevalue += "'<div style=\"width: 15em\">'+"; // 修改数字变更栏宽
titlevalue += "b.shortTitle";
//titlevalue += "+'</div>'"; // 不变更栏宽不要添加
titlevalue += ",";
title.push("刊名");
//titlevalue += "'<div style=\"width: 15em\">'+"; // 修改数字变更栏宽
titlevalue += "b.publicationTitle";
//titlevalue += "+'</div>'"; // 不变更栏宽不要添加
titlevalue += ",";
title.push("标签");
//titlevalue += "'<div style=\"width: 25em\">'+"; // 修改数字变更栏宽
titlevalue += "b.file.tags.values.join(' ')";
//titlevalue += "+'</div>'"; // 不变更栏宽不要添加
titlevalue += ",";
title.push("导出日期");
titlevalue += "'<div style=\"width: 7em\">'+"; // 修改数字变更栏宽
titlevalue += "getTimef(new Date(b.importDate)).slice(0,-8)";
titlevalue += "+'</div>'"; // 不变更栏宽不要添加
titlevalue += ",";
///---不要修改其他---///
titlevalue += "]);";
const metaeditEnabled = app.plugins.enabledPlugins.has("metaedit");
const thisFile = dv.pages().where((f) => f.file.path == dv.current().file.path);
///YAML数据
let vaultPath = dv.current().vaultPath;
let outType = dv.current().outType;
let searchTag = dv.current().searchTag;
let searchCodePro1 = dv.current().searchCodePro1;
let searchCodePro2 = dv.current().searchCodePro2;
let searchYear = dv.current().searchYear;
let searchMonth = dv.current().searchMonth;
let searchFinish = dv.current().searchFinish;
let searchPublicationTitle = dv.current().searchPublicationTitle;
let sortRule = dv.current().sortRule;
///插件判定
if (metaeditEnabled == true) {
  ///拉取metaeditapi
  const { update } = this.app.plugins.plugins["metaedit"].api;
  dv.el("IFPM", "", { cls: "root" });
  ///Warning
  ///DataView
  if (app.plugins.plugins.dataview.manifest.version.match(/0\.4\./) != null) {
    dv.el(
      "p",
      "🚨 <u>当前 DataView 为 " +
      app.plugins.plugins.dataview.manifest.version +
      "版本,为避免不必要的麻烦，建议更新为最新版本</u>",
      {
        attr: { style: "color:red;font-weight:900;font-size:14px" },
      }
    );
  }
  ///Tips
  ///CSS版本判断提示
  let cssOn = 0;
  for (let i = 0; i < app.customCss.extraStyleEls.length; i++) {
    if (
      app.customCss.extraStyleEls[i].innerText.indexOf(
        "/*--DKLN-V1.3.2-IFPM--*/"
      ) != -1
    ) {
      cssOn += 1;
    }
  }

  ///通用function
  ///获取当前时间并补位格式化
  function getTimef(ax) {
    let time = ax;
    let year = time.getFullYear();
    let month = time.getMonth() + 1;
    let date = time.getDate();
    let hour = time.getHours();
    let minute = time.getMinutes();
    let second = time.getSeconds();
    function timeAdd0(m) {
      return m < 10 ? "0" + m : m;
    }
    return (
      year +
      "-" +
      timeAdd0(month) +
      "-" +
      timeAdd0(date) +
      " " +
      timeAdd0(hour) +
      "_" +
      timeAdd0(minute) +
      "_" +
      timeAdd0(second)
    );
  }
  ///数组去重
  function unique(arr) {
    return Array.from(new Set(arr));
  }
  ///路径选择器
  const vaultPathDropdownMaker = (pn, fpath) => {
    const file = this.app.vault.getAbstractFileByPath(fpath);
    const arr = dv.pages().file.folder;
    let paths = Array.from(new Set(arr)).sort();
    let z = [];
    for (let i = 0; i < paths.length; i++) {
      if (paths[i] != "" && paths[i] != null) {
        z.push(paths[i]);
      }
    }
    paths = z;
    /// byonev6.0.4
    /// paths.unshift('""');
    const dropdown = this.container.createEl("select");
    paths.forEach((path, index) => {
      let opt = path;
      let el = dropdown.createEl("option");
      /// byonev6.0.4
      if (opt != '""') {
        el.textContent = opt;
        el.value = opt;
        dropdown.appendChild(el);
      }
    });
    paths.indexOf(vaultPath.toString()) < 0
      ? (dropdown.selectedIndex = 0)
      : (dropdown.selectedIndex = paths.indexOf(vaultPath.toString()));
    dropdown.addEventListener("change", async (evt) => {
      evt.preventDefault();
      await update(pn, paths[dropdown.selectedIndex], file);
    });
    return dropdown;
  };
  ///导出模式选择器
  const outTypeDropdownMaker = (pn, fpath) => {
    const file = this.app.vault.getAbstractFileByPath(fpath);
    const optionsText = ["MD", "CSV"];
    const optionsValue = ["md", "csv"];
    const dropdown = this.container.createEl("select");
    dropdown.style = "width:6em;text-align:center";
    const option1 = dropdown.createEl("option");
    option1.style = "text-align: left;";
    option1.text = optionsText[0];
    option1.value = optionsValue[0];
    const option2 = dropdown.createEl("option");
    option2.style = "text-align: left;";
    option2.text = optionsText[1];
    option2.value = optionsValue[1];
    dropdown.selectedIndex != null
      ? (dropdown.selectedIndex = optionsValue.indexOf(outType))
      : (dropdown.selectedIndex = 0);
    dropdown.addEventListener("change", async (evt) => {
      evt.preventDefault();
      await update(pn, optionsValue[dropdown.selectedIndex], file);
    });
    return dropdown;
  };
  ///年份选择器
  const yearDropdownMaker = (pn, fpath) => {
    const file = this.app.vault.getAbstractFileByPath(fpath);
    const arr = dv.pages().filter((t) => t.file.path.includes(vaultPath))
      .importDate.c.year;
    let years = Array.from(new Set(arr)).sort((a, b) => a - b);
    years = years.map(function (i) {
      return i + "年";
    });
    years.unshift("全部年");
    years.unshift("noyear");
    const dropdown = this.container.createEl("select");
    dropdown.style = "width:8em";
    years.forEach((year, index) => {
      let opt = year;
      let el = dropdown.createEl("option");
      opt != "noyear" ? (el.textContent = opt) : (el.textContent = "选择年份");
      el.value = opt;
      dropdown.appendChild(el);
    });
    years.indexOf(searchYear.toString()) < 0
      ? (dropdown.selectedIndex = 0)
      : (dropdown.selectedIndex = years.indexOf(searchYear.toString()));
    dropdown.addEventListener("change", async (evt) => {
      evt.preventDefault();
      await update(pn, years[dropdown.selectedIndex], file);
    });
    return dropdown;
  };
  ///月份选择器
  const monthDropdownMaker = (pn, fpath) => {
    const file = this.app.vault.getAbstractFileByPath(fpath);
    const arr = dv.pages().filter((t) => t.file.path.includes(vaultPath))
      .importDate.c.month;
    let months = Array.from(new Set(arr)).sort((a, b) => a - b);
    months.unshift();
    months = months.map(function (i) {
      return i + "月";
    });
    months.unshift("全部月");
    months.unshift("nomonth");
    const dropdown = this.container.createEl("select");
    dropdown.style = "width:8em";
    months.forEach((month, index) => {
      let opt = month;
      let el = dropdown.createEl("option");
      opt != "nomonth" ? (el.textContent = opt) : (el.textContent = "选择月份");
      el.value = opt;
      dropdown.appendChild(el);
    });
    months.indexOf(searchMonth.toString()) < 0
      ? (dropdown.selectedIndex = 0)
      : (dropdown.selectedIndex = months.indexOf(searchMonth.toString()));
    dropdown.addEventListener("change", async (evt) => {
      evt.preventDefault();
      await update(pn, months[dropdown.selectedIndex], file);
    });
    return dropdown;
  };
  ///标签选择器
  const tagsDropdownMaker = (pn, fpath) => {
    const file = this.app.vault.getAbstractFileByPath(fpath);
    const arr = dv.pages().filter((t) => t.file.path.includes(vaultPath))
      .file.tags;
    let tags = Array.from(new Set(arr)).sort();
    tags.unshift("#");
    tags = unique(tags);
    const dropdown = this.container.createEl("select");
    tags.forEach((tag, index) => {
      let opt = tag;
      let el = dropdown.createEl("option");
      opt != "#" ? (el.textContent = opt) : (el.textContent = "全部标签");
      el.value = opt;
      dropdown.appendChild(el);
    });
    tags.indexOf("#" + searchTag) < 0
      ? (dropdown.selectedIndex = 0)
      : (dropdown.selectedIndex = tags.indexOf("#" + searchTag));
    dropdown.addEventListener("change", async (evt) => {
      evt.preventDefault();
      await update(pn, tags[dropdown.selectedIndex].slice(1), file);
    });
    return dropdown;
  };
  ///进阶标签选择器1
  const tag1DropdownMaker = (pn, fpath) => {
    const file = this.app.vault.getAbstractFileByPath(fpath);
    const arr = dv.pages().filter((t) => t.file.path.includes(vaultPath))
      .file.tags;
    let tags = Array.from(new Set(arr)).sort();
    tags.unshift("#");
    tags = unique(tags);
    const dropdown = this.container.createEl("select");
    tags.forEach((tag, index) => {
      let opt = tag;
      let el = dropdown.createEl("option");
      opt != "#" ? (el.textContent = opt) : (el.textContent = "全部标签");
      el.value = opt;
      dropdown.appendChild(el);
    });
    tags.indexOf("#" + searchCodePro1) < 0
      ? (dropdown.selectedIndex = 0)
      : (dropdown.selectedIndex = tags.indexOf("#" + searchCodePro1));
    dropdown.addEventListener("change", async (evt) => {
      evt.preventDefault();
      await update(pn, tags[dropdown.selectedIndex].slice(1), file);
    });
    return dropdown;
  };
  ///进阶标签选择器2
  const tag2DropdownMaker = (pn, fpath) => {
    const file = this.app.vault.getAbstractFileByPath(fpath);
    const arr = dv.pages().filter((t) => t.file.path.includes(vaultPath))
      .file.tags;
    let tags = Array.from(new Set(arr)).sort();
    tags.unshift("#");
    tags = unique(tags);
    const dropdown = this.container.createEl("select");
    tags.forEach((tag, index) => {
      let opt = tag;
      let el = dropdown.createEl("option");
      opt != "#" ? (el.textContent = opt) : (el.textContent = "全部标签");
      el.value = opt;
      dropdown.appendChild(el);
    });
    tags.indexOf("#" + searchCodePro2) < 0
      ? (dropdown.selectedIndex = 0)
      : (dropdown.selectedIndex = tags.indexOf("#" + searchCodePro2));
    dropdown.addEventListener("change", async (evt) => {
      evt.preventDefault();
      await update(pn, tags[dropdown.selectedIndex].slice(1), file);
    });
    return dropdown;
  };
  ///阅读状态选择器
  const FinishDropdownMaker = (pn, fpath) => {
    const file = this.app.vault.getAbstractFileByPath(fpath);
    const optionsText = ["全部", "已读", "在读", "未读"];
    const optionsValue = ["All", "Done", "reading", "unread"];
    const dropdown = this.container.createEl("select");
    dropdown.style = "width:6em;text-align:center";
    const option1 = dropdown.createEl("option");
    option1.style = "text-align: left;";
    option1.text = optionsText[0];
    option1.value = optionsValue[0];
    const option2 = dropdown.createEl("option");
    option2.style = "text-align: left;";
    option2.text = optionsText[1];
    option2.value = optionsValue[1];
    const option3 = dropdown.createEl("option");
    option3.style = "text-align: left;";
    option3.text = optionsText[2];
    option3.value = optionsValue[2];
    const option4 = dropdown.createEl("option");
    option4.style = "text-align: left;";
    option4.text = optionsText[3];
    option4.value = optionsValue[3];
    dropdown.selectedIndex != null
      ? (dropdown.selectedIndex = optionsValue.indexOf(searchFinish.toString()))
      : (dropdown.selectedIndex = 0);
    dropdown.addEventListener("change", async (evt) => {
      evt.preventDefault();
      await update(pn, optionsValue[dropdown.selectedIndex], file);
    });
    return dropdown;
  };
  ///刊名选择器
  const publicationTitleDropdownMaker = (pn, fpath) => {
    const file = this.app.vault.getAbstractFileByPath(fpath);
    const arr = dv
      .pages()
      .filter((t) => t.file.path.includes(vaultPath)).publicationTitle;
    let publicationTitle = Array.from(new Set(arr)).sort();
    let temp = [];
    for (let i = 0; i < publicationTitle.length; i++) {
      if (typeof publicationTitle[i] == "string") {
        temp = temp.concat(publicationTitle[i]);
      } else {
        temp = temp.concat(publicationTitle[i].path);
      }
    }
    publicationTitle = temp;
    temp = null;
    publicationTitle.unshift("All");
    publicationTitle = unique(publicationTitle);
    const dropdown = this.container.createEl("select");
    publicationTitle.forEach((publicationTitlex, index) => {
      let opt = publicationTitlex;
      let el = dropdown.createEl("option");
      opt != "All" ? (el.textContent = opt) : (el.textContent = "全部期刊");
      el.value = opt;
      dropdown.appendChild(el);
    });
    publicationTitle.indexOf(searchPublicationTitle) < 0
      ? (dropdown.selectedIndex = 0)
      : (dropdown.selectedIndex = publicationTitle.indexOf(
        searchPublicationTitle
      ));
    dropdown.addEventListener("change", async (evt) => {
      evt.preventDefault();
      await update(pn, publicationTitle[dropdown.selectedIndex], file);
    });
    return dropdown;
  };

  ///排序选择器
  const sortRuleDropdownMaker = (pn, fpath) => {
    const file = this.app.vault.getAbstractFileByPath(fpath);
    const optionsText = [
      "被引次数降序",
      "被引次数升序",
      "导出日期降序",
      "导出日期升序",
      "影响因子降序",
      "影响因子升序",
      "分区降序",
      "分区升序",
      "分类降序",
      "分类升序",
      "刊名降序",
      "刊名升序",
      "作者降序",
      "作者升序",
    ];
    const optionsValue = [
      "archiveLocation",
      "archiveLocationUp",
      "importDate",
      "importDateUp",
      "callNumber",
      "callNumberUp",
      "libraryCatalog",
      "libraryCatalogUp",
      "collection",
      "collectionUp",
      "publicationTitle",
      "publicationTitleUp",
      "creators",
      "creatorsUp",
    ];
    const dropdown = this.container.createEl("select");
    dropdown.style = "width:11em;";
    const option1 = dropdown.createEl("option");
    option1.style = "text-align left;";
    option1.text = optionsText[0];
    option1.value = optionsValue[0];
    const option2 = dropdown.createEl("option");
    option2.style = "text-align left;";
    option2.text = optionsText[1];
    option2.value = optionsValue[1];
    const option3 = dropdown.createEl("option");
    option3.style = "text-align left;";
    option3.text = optionsText[2];
    option3.value = optionsValue[2];
    const option4 = dropdown.createEl("option");
    option4.style = "text-align left;";
    option4.text = optionsText[3];
    option4.value = optionsValue[3];
    const option5 = dropdown.createEl("option");
    option5.style = "text-align left;";
    option5.text = optionsText[4];
    option5.value = optionsValue[4];
    const option6 = dropdown.createEl("option");
    option6.style = "text-align left;";
    option6.text = optionsText[5];
    option6.value = optionsValue[5];
    const option7 = dropdown.createEl("option");
    option7.style = "text-align left;";
    option7.text = optionsText[6];
    option7.value = optionsValue[6];
    const option8 = dropdown.createEl("option");
    option8.style = "text-align left;";
    option8.text = optionsText[7];
    option8.value = optionsValue[7]; const option9 = dropdown.createEl("option");
    option9.style = "text-align left;";
    option9.text = optionsText[8];
    option9.value = optionsValue[8]; const option10 = dropdown.createEl("option");
    option10.style = "text-align  left;";
    option10.text = optionsText[9];
    option10.value = optionsValue[9]; const option11 = dropdown.createEl("option");
    option11.style = "text-align  left;";
    option11.text = optionsText[10];
    option11.value = optionsValue[10]; const option12 = dropdown.createEl("option");
    option12.style = "text-align  left;";
    option12.text = optionsText[11];
    option12.value = optionsValue[11]; const option13 = dropdown.createEl("option");
    option13.style = "text-align  left;";
    option13.text = optionsText[12];
    option13.value = optionsValue[12]; const option14 = dropdown.createEl("option");
    option14.style = "text-align  left;";
    option14.text = optionsText[13];
    option14.value = optionsValue[13];
    dropdown.selectedIndex != null
      ? (dropdown.selectedIndex = optionsValue.indexOf(sortRule))
      : (dropdown.selectedIndex = 0);
    dropdown.addEventListener("change", async (evt) => {
      evt.preventDefault();
      await update(pn, optionsValue[dropdown.selectedIndex], file);
    });
    return dropdown;
  };
  ///头部渲染
  dv.el("IFPM", "", { cls: "importDate" });
  dv.el("b", "检索路径:&emsp;&ensp;");
  vaultPathDropdownMaker("vaultPath", dv.current().file.path);
  dv.el("br");
  dv.el("br");
  dv.el("b", "检索时间:&emsp;&ensp;");
  yearDropdownMaker("searchYear", dv.current().file.path);
  dv.el("b", "&emsp;");
  monthDropdownMaker("searchMonth", dv.current().file.path);
  dv.el("br");
  dv.el("br");
  dv.el("b", "阅读状态:&emsp;&ensp;");
  FinishDropdownMaker("searchFinish", dv.current().file.path);
  dv.el("br");
  dv.el("br");
  dv.el("b", "选择标签1:&emsp;");
  tagsDropdownMaker("searchTag", dv.current().file.path);
  dv.el("br");
  dv.el("br");
  dv.el("b", "选择标签2:&emsp;");
  tag1DropdownMaker("searchCodePro1", dv.current().file.path);
  dv.el("br");
  dv.el("br");
  dv.el("b", "选择标签3:&emsp;");
  tag2DropdownMaker("searchCodePro2", dv.current().file.path);
  dv.el("br");
  dv.el("br");
  dv.el("b", "选择期刊:&emsp;&ensp;");
  publicationTitleDropdownMaker(
    "searchPublicationTitle",
    dv.current().file.path
  );
  dv.el("br");
  dv.el("br");
  dv.el("b", "排序条件:&emsp;&ensp;");
  sortRuleDropdownMaker("sortRule", dv.current().file.path);
  ///移动端判断
  if (app.isMobile == false) {
    dv.el("br");
    dv.el("br");
    dv.el("b", "导出格式:&emsp;&ensp;");
    outTypeDropdownMaker("outType", dv.current().file.path);
  }
  ///计算
  let searchQuery = "outputs = dv.pages()";
  ///时间计算
  if (searchMonth != "nomonth" && searchYear != "noyear") {
    if (searchMonth != "全部月" && searchYear != "全部年") {
      searchYear = parseInt(searchYear);
      searchMonth = parseInt(searchMonth);
      searchQuery +=
        ".filter((t) =>new Date(t.importDate).getFullYear()==" +
        searchYear +
        " && new Date(t.importDate).getMonth()+1==" +
        searchMonth +
        ")";
      searchYear = dv.current().searchYear;
      searchMonth = dv.current().searchMonth;
    } else if (searchMonth == "全部月" && searchYear != "全部年") {
      searchYear = parseInt(searchYear);
      searchMonth = "";
      searchQuery +=
        ".filter((t) =>new Date(t.importDate).getFullYear()==" +
        searchYear +
        ")";
      searchYear = dv.current().searchYear;
    } else if (searchMonth != "全部月" && searchYear == "全部年") {
      searchYear = "";
      searchMonth = parseInt(searchMonth);
      searchQuery +=
        ".filter((t) =>new Date(t.importDate).getMonth()+1==" +
        searchMonth +
        ")";
      searchMonth = dv.current().searchMonth;
    } else if (searchMonth == "全部月" && searchYear == "全部年") {
      searchYear = "";
      searchMonth = "";
      searchQuery += ".filter((t) =>t.importDate)";
    }
    ///标签计算
    if (searchTag && searchCodePro1 && searchCodePro2) {
      searchQuery +=
        ".filter((b) => b.file.tags.indexOf('#'+'" +
        searchTag +
        "') != -1)" +
        ".filter((b) => b.file.tags.indexOf('#'+'" +
        searchCodePro1 +
        "') != -1)" +
        ".filter((b) => b.file.tags.indexOf('#'+'" +
        searchCodePro2 +
        "') != -1)";
      searchTag =
        "含有" +
        " #" +
        searchTag +
        " #" +
        searchCodePro1 +
        " #" +
        searchCodePro2 +
        " 标签的文献";
    } else if (
      searchTag &&
      searchCodePro1 &&
      !searchCodePro2
    ) {
      searchQuery +=
        ".filter((b) => b.file.tags.indexOf('#'+'" +
        searchTag +
        "') != -1)" +
        ".filter((b) => b.file.tags.indexOf('#'+'" +
        searchCodePro1 +
        "') != -1)";
      searchTag =
        "含有" + " #" + searchTag + " #" + searchCodePro1 + " 标签的文献";
    } else if (
      searchTag &&
      !searchCodePro1 &&
      searchCodePro2
    ) {
      searchQuery +=
        ".filter((b) => b.file.tags.indexOf('#'+'" +
        searchTag +
        "') != -1)" +
        ".filter((b) => b.file.tags.indexOf('#'+'" +
        searchCodePro2 +
        "') != -1)";
      searchTag =
        "含有" + " #" + searchTag + " #" + searchCodePro2 + " 标签的文献";
    } else if (
      searchTag &&
      !searchCodePro1 &&
      !searchCodePro2
    ) {
      searchQuery +=
        ".filter((b) => b.file.tags.indexOf('#'+'" + searchTag + "') != -1)";
      searchTag = "含有" + " #" + searchTag + " 标签的文献";
    } else if (
      !searchTag &&
      searchCodePro1 &&
      searchCodePro2
    ) {
      searchQuery +=
        ".filter((b) => b.file.tags.indexOf('#'+'" +
        searchCodePro1 +
        "') != -1)" +
        ".filter((b) => b.file.tags.indexOf('#'+'" +
        searchCodePro2 +
        "') != -1)";
      searchTag =
        "含有" + " #" + searchCodePro1 + " #" + searchCodePro2 + " 标签的文献";
    } else if (
      !searchTag &&
      searchCodePro1 &&
      !searchCodePro2
    ) {
      searchQuery +=
        ".filter((b) => b.file.tags.indexOf('#'+'" +
        searchCodePro1 +
        "') != -1)";
      searchTag = "含有" + " #" + searchCodePro1 + " 标签的文献";
    } else if (
      !searchTag &&
      !searchCodePro1 &&
      searchCodePro2
    ) {
      searchQuery +=
        ".filter((b) => b.file.tags.indexOf('#'+'" +
        searchCodePro2 +
        "') != -1)";
      searchTag = "含有" + " #" + searchCodePro2 + " 标签的文献";
    } else if (
      !searchTag &&
      !searchCodePro1 &&
      !searchCodePro2
    ) {
      searchTag = '';
    }
    ///完成状态计算
    if (searchFinish == "All") {
      searchQuery += "";
    } else {
      searchQuery +=
        ".filter((t) => t.file.tags.toString().includes('" +
        searchFinish +
        "'))";
    }
    ///路径计算
    if (vaultPath == "") {
      searchQuery += "";
    } else {
      searchQuery +=
        ".filter((t) => t.file.folder.includes('" + vaultPath + "'))";
    }
    ///期刊计算
    if (searchPublicationTitle == "All") {
      searchQuery += "";
    } else {
      searchQuery +=
        ".filter((t) =>t.publicationTitle)" +
        ".filter((t) =>t.publicationTitle=='" +
        searchPublicationTitle +
        "'||t.publicationTitle.path=='" +
        searchPublicationTitle +
        "')";
      searchPublicationTitle = "《" + searchPublicationTitle + "》期刊中";
    }
    ///综合计算
    let outputs = "";
    searchQuery += ".sort((a,b)=>{return -a." + sortRule + "})";
    eval(searchQuery);

    /// byonev6.0.4
    searchPublicationTitle = searchPublicationTitle === "All" ? "" : searchPublicationTitle;

    if (sortRule != null && sortRule.includes("Up")) {
      sortRule = sortRule.substring(0, sortRule.length - 2);
      searchQuery += ".sort((a,b)=>{return -a." + sortRule + "})";

    }

    if (searchFinish == "All") {
      searchFinish =
        "共导出" +
        searchPublicationTitle +
        searchTag +
        "【" +
        outputs.length +
        "】篇";
    }
    if (searchFinish == "Done") {
      searchFinish =
        "已读完" +
        searchPublicationTitle +
        searchTag +
        "【" +
        outputs.length +
        "】篇";
    }
    if (searchFinish == "reading") {
      searchFinish =
        "正在阅读" +
        searchPublicationTitle +
        searchTag +
        "【" +
        outputs.length +
        "】篇";
    }
    if (searchFinish == "unread") {
      searchFinish =
        "有【" +
        outputs.length +
        "】篇" +
        searchPublicationTitle +
        searchTag +
        "尚未读过";
    }
    dv.paragraph("#### " + searchYear + searchMonth + "</br>" + searchFinish);
    eval(titlevalue);
    ///导出
    ///移动端判断
    if (app.isMobile == false) {
      ///内容
      let exportButton = document.createElement("a");
      let content;
      if (outType == "md") {
        content =
          "> [!info] <center>" +
          searchYear +
          searchMonth +
          "</br>" +
          searchFinish +
          "</center>\n\n";
        for (let i = 0; i < outputs.length; i++) {
          content += "> [!note]- " + outputs[i][0] + "\n>> |||\n>> |--:|--|\n";
          for (let z = 1; z < outputs[i].length; z++) {
            content +=
              ">> |<div style='width:5em'>" +
              title[z] +
              "</div>|" +
              outputs[i][z] +
              "|\n";
          }
          content += "\n";
        }
        exportButton.download = "IFPM Export " + getTimef(new Date()) + ".md";
      } else if (outType == "csv") {
        content = title.join(",") + "\n";
        for (let i = 0; i < outputs.length; i++) {
          content += '"' + outputs[i].join('","') + '"\n';
        }
        content = "\ufeff" + content;
        exportButton.download = "IFPM Export " + getTimef(new Date()) + ".csv";
      }
      ///导出button
      let ba64 =
        "data:text/plain;base64," +
        Buffer.from(content, "utf-8").toString("base64");
      exportButton.innerHTML = "点击导出";
      exportButton.href = ba64;
      dv.el("center", exportButton, { cls: "exportButton" });
    }
    ///表格渲染
    dv.el("br", "");
    dv.el("div", dv.markdownTable(title, outputs));
  } else {
    dv.el("br");
    dv.el("br");
    dv.el("b", "### 请完成选择");
  }
}
///插件不全
else {
  dv.el("br", "");
  dv.el("b", "# 请安装并启用插件【MetaEdit】");
}
TimeMonitor();
console.log("总耗时 " + timeCount.toString() + " --> " + (TimeList["Time" + timeCount] - TimeList["Time0"]).toString() + " ms");