(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-53f91dda"],{"2d06":function(t,a,e){"use strict";e("8660")},8660:function(t,a,e){},a523:function(t,a,e){"use strict";e("4de4"),e("b64b"),e("2ca0"),e("99af"),e("20f6"),e("4b85"),e("498a"),e("a15b");var r=e("2b0e");function n(t){return r["a"].extend({name:"v-".concat(t),functional:!0,props:{id:String,tag:{type:String,default:"div"}},render:function(a,e){var r=e.props,n=e.data,s=e.children;n.staticClass="".concat(t," ").concat(n.staticClass||"").trim();var i=n.attrs;if(i){n.attrs={};var o=Object.keys(i).filter((function(t){if("slot"===t)return!1;var a=i[t];return t.startsWith("data-")?(n.attrs[t]=a,!1):a||"string"===typeof a}));o.length&&(n.staticClass+=" ".concat(o.join(" ")))}return r.id&&(n.domProps=n.domProps||{},n.domProps.id=r.id),a(r.tag,n,s)}})}var s=e("d9f7");a["a"]=n("container").extend({name:"v-container",functional:!0,props:{id:String,tag:{type:String,default:"div"},fluid:{type:Boolean,default:!1}},render:function(t,a){var e,r=a.props,n=a.data,i=a.children,o=n.attrs;return o&&(n.attrs={},e=Object.keys(o).filter((function(t){if("slot"===t)return!1;var a=o[t];return t.startsWith("data-")?(n.attrs[t]=a,!1):a||"string"===typeof a}))),r.id&&(n.domProps=n.domProps||{},n.domProps.id=r.id),t(r.tag,Object(s["a"])(n,{staticClass:"container",class:Array({"container--fluid":r.fluid}).concat(e||[])}),i)}})},dfc3:function(t,a,e){"use strict";e.r(a);var r=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("v-container",{staticClass:"pa-4",attrs:{fluid:""}},[0==t.workplaces.length?e("div",{staticClass:"d-flex align-center justify-center mt-6",staticStyle:{width:"100%"}},[e("v-progress-circular",{attrs:{size:"72",color:"primary",indeterminate:""}})],1):e("div",[e("div",{staticClass:"text-h6 mb-4"},[t._v(" Опыт работы: "+t._s(t.format_summary()))]),e("v-list",t._l(t.workplaces,(function(a){return e("v-list-item",{key:a.id,staticClass:"flex-column align-start mb-6 px-0"},[e("div",{staticClass:"align-self-start text-overline work-title pl-0"},[t._v(t._s(a.name))]),e("div",{staticClass:"text-overline"},[t._v(" "+t._s(t.format_date(a.date_start))+" — "+t._s(a.by_today?"по сегодняшний день":t.format_date(a.date_end))+" ")]),e("v-list-item-content",{staticClass:"text-body-2 align-self-start pt-1",domProps:{innerHTML:t._s(a.description)}})],1)})),1)],1)])},n=[],s=e("5530"),i=(e("99af"),e("159b"),e("2f62")),o={name:"WorkPlaces",data:function(){return{summary:0}},computed:Object(s["a"])({},Object(i["b"])(["workplaces"])),mounted:function(){var t=this;this.$store.dispatch("fetch_workplaces").then((function(){t.summary_time()}))},methods:{format_date:function(t){var a=["янв.","фев.","мар.","апр.","май","июнь","июль","авг.","сен.","окт.","ноя.","дек."],e=new Date(t);return"".concat(a[e.getMonth()]," ").concat(e.getFullYear())},format_summary:function(){var t=new Date(this.summary);return"".concat(t.getFullYear()-1970," год, ").concat(t.getMonth()+1," мес.")},summary_time:function(){var t=this;this.workplaces.forEach((function(a){var e=new Date(a.date_start),r=a.by_today?new Date:new Date(a.date_end);t.summary+=new Date(r-e).getTime()}))}}},c=o,d=(e("2d06"),e("2877")),l=e("6544"),u=e.n(l),f=e("a523"),m=e("8860"),p=e("da13"),v=e("5d23"),_=e("490a"),y=Object(d["a"])(c,r,n,!1,null,"91232c5a",null);a["default"]=y.exports;u()(y,{VContainer:f["a"],VList:m["a"],VListItem:p["a"],VListItemContent:v["a"],VProgressCircular:_["a"]})}}]);
//# sourceMappingURL=chunk-53f91dda.6e2fea7c.js.map