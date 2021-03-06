import Base from '../../utils/base.js'

const http = new Base()
var app = getApp();


Page({
    data: {
        indicatorDots: true,
        autoplay: true,
        interval: 3000,
        duration: 1000,
        loadingHidden: false, // loading
        swiperCurrent: 0,
        categories: [],
        activeCategoryId: 0,
        goods: [],
        scrollTop: "0",
        loadingMoreHidden: true,
        searchInput: '',
        p: 1,
        processing: false
    },
    onLoad: function () {
        var that = this;
        wx.setNavigationBarTitle({
            title: app.globalData.shopName
        });
    },
    //解决切换不刷新，每次展示都会调用这个方法
    onShow: function () {
        this.getBannerAndCat();
    },
    scroll: function (e) {
        var that = this, 
            scrollTop = that.data.scrollTop;
        that.setData({
            scrollTop: e.detail.scrollTop
        });
    },
    //事件处理函数
    swiperchange: function (e) {
        this.setData({
            swiperCurrent: e.detail.current
        })
    },
    listenerSearchInput: function (e) {
        this.setData({
            searchInput: e.detail.value
        });
    },
    toSearch: function (e) {
        this.setData({
            p: 1,
            goods: [],
            loadingMoreHidden: true
        });
        this.getFoodList();
    },
    tapBanner: function (e) {
        if (e.currentTarget.dataset.id != 0) {
            wx.navigateTo({
                url: "/pages/food/info?id=" + e.currentTarget.dataset.id
            });
        }
    },
    toDetailsTap: function (e) {
        wx.navigateTo({
            url: "/pages/food/info?id=" + e.currentTarget.dataset.id
        });
    },
    getBannerAndCat: function () {
        var that = this;
        http.request({
            url: '/food/index',
            sCallback: res => {
                that.setData({
                    banners: res.banner_list,
                    categories: res.cat_list
                });
                that.getFoodList();
            },
            eCallback: res => {
                app.alert({"content": res.msg});
            }
        });
    },
    catClick: function (e) {
        this.setData({
            activeCategoryId: e.currentTarget.dataset.id
        });
        this.setData({
            loadingMoreHidden: true,
            p: 1,
            goods: []
        });
        this.getFoodList();
    },
    onReachBottom: function () {
        var that = this;
        setTimeout(function () {
            that.getFoodList();
        }, 500);
    },
    getFoodList: function () {
        var that = this;
        if (that.data.processing) {
            return;
        }

        if (!that.data.loadingMoreHidden) {
            return;
        }

        that.setData({
            processing: true
        });
        http.request({
            url: '/food/search',
            method: 'POST',
            data: {
                cat_id: that.data.activeCategoryId,
                query_key: that.data.searchInput,
                page: that.data.p,
            },
            sCallback: res => {
                var goods = res.list;
                that.setData({
                    goods: that.data.goods.concat(goods),
                    p: that.data.p + 1,
                    processing: false
                });
                if (res.has_more == 0) {
                    that.setData({
                        loadingMoreHidden: false
                    });
                }
            },
            eCallback: res => {
                app.alert({"content": res.msg});
            }
        })
    }
});
