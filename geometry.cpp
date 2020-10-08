#include <bits/stdc++.h>
using namespace std;

typedef long double ld;
typedef long long ll;

const int INF = 1e5, MOD = 1e9 + 7;
const ld EPS = 1e-9, PI = acos(-1);

struct Point
{
    ld x, y;
    Point()
    {
        x = 0.0, y = 0.0;
    }
    Point(ld a, ld b)
    {
        x = a, y = b;
    }
    Point operator -(const Point &other) const
    {
        return Point(x - other.x, y - other.y);
    }
    Point operator +(const Point &other) const
    {
        return Point(x + other.x, y + other.y);
    }
    Point operator *(const ld &d) const
    {
        return Point(x * d, y * d);
    }
    bool operator ==(const Point &other) const
    {
        return abs(x - other.x) < EPS && abs(y - other.y) < EPS;
    }
    bool operator <(const Point &other) const
    {
        return x + EPS < other.x || (abs(x - other.x) < EPS && y + EPS < other.y);
    }
    ld mod() const
    {
        return hypot(x, y);
    }
    Point norm() const
    {
        return Point(x / hypot(x, y), y / hypot(x, y));
    }
};

struct Line
{
    ld a, b, c;
    Line()
    {
        a = 0.0, b = 0.0, c = 0.0;
    }
    Line(ld x, ld y, ld z)
    {
        a = x, b = y, c = z;
    }
    Line(Point n, Point m)
    {
        a = n.y - m.y;
        b = m.x - n.x;
        c = -a * n.x - b * n.y;
    }
    Line(Point p, ld x, ld y)
    {
        a = y;
        b = -x;
        c = -a * p.x - b * p.y;
    }
    Point norm() const
    {
        return Point(a, b);
    }
    bool check(const Point &p) const
    {
        return abs(a * p.x + b * p.y + c) < EPS;
    }
};

istream &operator >>(istream &in, Point &p)
{
    in >> p.x >> p.y;
    return in;
}

ostream &operator <<(ostream &out, Point &p)
{
    out << p.x << " " << p.y;
    return out;
}

ld dot_p(Point a, Point b)
{
    return a.x * b.x + a.y * b.y;
}

ld cross_p(Point a, Point b)
{
    return a.x * b.y - a.y * b.x;
}

ld dist(Point a, Point b)
{
    return (a - b).mod();
}

ld line_dist(Point a, Line p)
{
    return abs(p.a * a.x + p.b * a.y + p.c) / hypot(p.a, p.b);
}

ld segm_dist(Point l, Point r, Point a)
{
    if (l == a || r == a)
        return 0.0;
    if (dot_p(r - l, a - l) < 0)
        return dist(a, l);
    else if (dot_p(l - r, a - r) < 0)
        return dist(a, r);
    else
    {
        Line segm(l, r);
        return line_dist(a, segm);
    }
}

bool inter(Point a, Point b, Point c, Point d)
{
    Line f(a, b), s(c, d);
    int up1 = f.c * s.b - f.b * s.c;
    int up2 = f.a * s.c - s.a * f.c;
    int down = s.a * f.b - f.a * s.b;
    if (!down || (abs(up1) % abs(down)) || (abs(up2) % abs(down)))
        return false;
    Point result((ld)up1 / (ld)down, (ld)up2 / (ld)down);
    return (segm_dist(a, b, result) < EPS) && (segm_dist(c, d, result) < EPS);
}

int gcd(int a, int b)
{
    if (a < b)
        swap(a, b);
    if (!b)
        return a;
    return gcd(a % b, b);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cout.precision(10);
    int n;
    ld r;
    cin >> n >> r;
    vector<Point> p(n);
    for (int i = 0; i < n; ++i)
        cin >> p[i];
    ld ans = 0;
    for (int i = 0; i < n; ++i)
    {
        int counter = 0;
        for (int j = 0; j < INF; ++j)
        {
            ld x = (ld)rand() / RAND_MAX;
            ld y = (ld)rand() / RAND_MAX;
            if (dist(p[i], Point(x, y)) < r - EPS)
                counter++;
        }
        ans += (ld)counter / INF;
    }
    cout << ans << endl;
    return 0;
}
